import React, { useEffect } from "react"
import Masonry from "react-masonry-component"
import "./Explore.css"
import { useDispatch, useSelector } from "react-redux"
import { getAllPhotosThunk } from "../../store/photo"
import { useHistory } from "react-router-dom"

function Explore() {
    const photosObj = useSelector(function (state) {
        return state.photoReducer.allPhotos
    })

    const photosArray = Object.values(photosObj)

    const dispatch = useDispatch()

    const history = useHistory()

    useEffect(() => {
        dispatch(getAllPhotosThunk())
    }, [dispatch]);

    return (
        <>
            <div className='spacerDiv'></div>
            <div className='fullExplorePage'>
                <h1 className='exploreHeader'>Explore</h1>
                <div className='masonryDiv'>
                    <Masonry
                        className={"masonryGrid"}
                        elementType={"div"}
                        options={{
                            fitWidth: true,
                            columnWidth: 1
                        }}
                        disableImagesLoaded={false}
                        updateOnEachImageLoad={false}
                    >
                        {photosArray.toReversed().map((photo, id) => {
                            return (
                                <div onClick={() => history.push(`/photos/${photo.id}`)} key={id} className="masonryItem changeCursor">
                                    <div className='divOverPhoto'>
                                        <div className='leftSideHoverInfo'>{photo.user_id}</div>
                                        <div className='rightSideHoverInfo'></div>

                                    </div>
                                    <img
                                        src={photo.photo}
                                        style={{ height: 300, margin: "0px 2px 0px 2px" }}
                                        alt='photo'
                                    />

                                </div>
                            );
                        })}
                    </Masonry>
                </div>
            </div>
        </>
    )
}

export default Explore
