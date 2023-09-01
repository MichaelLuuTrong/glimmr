import { useEffect, useState } from "react"
import "./Explore.css"
import { useDispatch, useSelector } from "react-redux"
import { getAllPhotosThunk } from "../../store/photo"
import { getAllUsersThunk } from "../../store/user"
import { useHistory } from "react-router-dom"
import InfiniteScroll from "react-infinite-scroll-component"

function Explore() {
    const photosObj = useSelector(state => state.photoReducer.allPhotos);
    const usersObj = useSelector(state => state.userReducer.allUsers)
    const photosArray = Object.values(photosObj)
    const usersArray = Object.values(usersObj)
    const dispatch = useDispatch()
    const history = useHistory()

    const [hasMore, setHasMore] = useState(true)
    const [pageNum, setPageNum] = useState(1)
    const [displayedPhotos, setDisplayedPhotos] = useState([]);
    const itemsPerPage = 39

    function getFirstNameById(usersArray, id) {
        const user = usersArray.find(user => user.id === id);
        return user ? user.first_name : null;
    }

    function getLastNameById(usersArray, id) {
        const user = usersArray.find(user => user.id === id);
        return user ? user.last_name : null;
    }

    function sortByCreatedAt(array) {
        return array.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
    }

    const fetchMoreData = () => {
        const newPageNum = pageNum + 1
        setPageNum(newPageNum)

        const startIndex = (newPageNum - 1) * itemsPerPage
        const endIndex = startIndex + itemsPerPage

        if (endIndex >= photosArray.length) {
            setHasMore(false)
            return
        }

        const newPhotosBatch = photosArray.slice(startIndex, endIndex)
        const updatedDisplayedPhotos = displayedPhotos.concat(newPhotosBatch)

        setDisplayedPhotos(updatedDisplayedPhotos)
    }

    useEffect(() => {
        dispatch(getAllPhotosThunk())
        dispatch(getAllUsersThunk())
    }, [dispatch]);

    useEffect(() => {
        const sortedPhotos = sortByCreatedAt(photosArray).reverse().slice(0, pageNum * itemsPerPage);
        setDisplayedPhotos(sortedPhotos);
    }, [photosArray, pageNum, itemsPerPage]);

    return (
        <>
            <div className='explorePageWrapper'>
                <div className='spacerDiv'></div>
                <div className='fullExplorePage'>
                    <h1 className='exploreHeader'>Explore</h1>
                    <InfiniteScroll
                        dataLength={pageNum * itemsPerPage}
                        next={fetchMoreData}
                        hasMore={hasMore}
                        loader={
                            <div className='loadingPhotosDiv'>
                                <img className='loadingIcon' src='https://media.tenor.com/wpSo-8CrXqUAAAAi/loading-loading-forever.gif' alt="loading icon" />
                                <div> Loading photos...</div>
                            </div>

                        }
                        endMessage={
                            <div className='noMorePhotosContainer'>
                                <div className="noMorePhotosDiv">
                                    You've reached the end! Thanks for looking!
                                </div>
                            </div>
                        }
                    >
                        <div className='masonryDiv'>
                            {displayedPhotos.map((photo, id) => {
                                return (
                                    <div onClick={() =>
                                        history.push(`/photos/${photo.id}`)} key={id}
                                        className="photoWithHoverDiv changeCursor">
                                        <div className='divOverPhotoExplore'>
                                            <div className='leftSideHoverInfo'>
                                                <div className='hoverPhotoTitle'>
                                                    {photo.title}</div>
                                                <div className='hoverPhotoTakerName'>
                                                    by {getFirstNameById(usersArray, photo.user_id)}
                                                    {" "}
                                                    {getLastNameById(usersArray, photo.user_id)}
                                                </div>
                                            </div>
                                            <div className='rightSideHoverInfo'>
                                                <div className='hoverFavoriteCount'>
                                                    <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512"><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.6 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z" /></svg>
                                                    {photo.favorites_count}</div>
                                                <div className='hoverCommentCount'>
                                                    <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><path d="M123.6 391.3c12.9-9.4 29.6-11.8 44.6-6.4c26.5 9.6 56.2 15.1 87.8 15.1c124.7 0 208-80.5 208-160s-83.3-160-208-160S48 160.5 48 240c0 32 12.4 62.8 35.7 89.2c8.6 9.7 12.8 22.5 11.8 35.5c-1.4 18.1-5.7 34.7-11.3 49.4c17-7.9 31.1-16.7 39.4-22.7zM21.2 431.9c1.8-2.7 3.5-5.4 5.1-8.1c10-16.6 19.5-38.4 21.4-62.9C17.7 326.8 0 285.1 0 240C0 125.1 114.6 32 256 32s256 93.1 256 208s-114.6 208-256 208c-37.1 0-72.3-6.4-104.1-17.9c-11.9 8.7-31.3 20.6-54.3 30.6c-15.1 6.6-32.3 12.6-50.1 16.1c-.8 .2-1.6 .3-2.4 .5c-4.4 .8-8.7 1.5-13.2 1.9c-.2 0-.5 .1-.7 .1c-5.1 .5-10.2 .8-15.3 .8c-6.5 0-12.3-3.9-14.8-9.9c-2.5-6-1.1-12.8 3.4-17.4c4.1-4.2 7.8-8.7 11.3-13.5c1.7-2.3 3.3-4.6 4.8-6.9c.1-.2 .2-.3 .3-.5z" /></svg>
                                                    {photo.comments_count}</div>
                                            </div>
                                        </div>
                                        <img
                                            className='displayPhoto'
                                            src={photo.thumbnail_photo}
                                            style={{ height: 300 }}
                                            alt=''
                                        />
                                    </div>
                                );
                            })}
                        </div>
                    </InfiniteScroll>
                </div >
            </div>
            <div className="exploreFooterDiv">
                <div className='myName'>
                    Website by Michael Luu-Trong
                </div>
                <div className='footerLinksDiv'>
                    <a className='footerLink' target="_blank" href='https://www.linkedin.com/in/michael-luu-trong-b52590286'>
                        <svg className='linkedin' xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" /></svg>
                    </a>
                    <a className='footerLink' target="_blank" href='https://github.com/MichaelLuuTrong'>
                        <svg className='github' xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" /></svg>
                    </a>
                    <a className='footerLink' target="_blank" href="https://www.michaelluutrong.com">
                        <svg className='personal' xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm7.753 18.305c-.261-.586-.789-.991-1.871-1.241-2.293-.529-4.428-.993-3.393-2.945 3.145-5.942.833-9.119-2.489-9.119-3.388 0-5.644 3.299-2.489 9.119 1.066 1.964-1.148 2.427-3.393 2.945-1.084.25-1.608.658-1.867 1.246-1.405-1.723-2.251-3.919-2.251-6.31 0-5.514 4.486-10 10-10s10 4.486 10 10c0 2.389-.845 4.583-2.247 6.305z" /></svg>
                    </a >
                    <a className='footerLink' target="_blank" href="mailto:michaelluutrong@gmail.com">
                        <svg className='email' xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 .02c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm6.99 6.98l-6.99 5.666-6.991-5.666h13.981zm.01 10h-14v-8.505l7 5.673 7-5.672v8.504z" /></svg>
                    </a >
                </div>
            </div>
        </>
    )
}

export default Explore
