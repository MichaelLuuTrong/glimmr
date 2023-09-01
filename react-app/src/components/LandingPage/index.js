import "./LandingPage.css"
import { NavLink } from 'react-router-dom'
import { useState, useEffect } from 'react'

import image1 from './BackgroundImages/image1.jpg'
import image2 from './BackgroundImages/image2.jpg'
import image3 from './BackgroundImages/image3.jpg'
import image4 from './BackgroundImages/image4.jpg'
import image5 from './BackgroundImages/image5.jpg'
import image6 from './BackgroundImages/image6.jpg'
import image7 from './BackgroundImages/image7.jpg'
import image8 from './BackgroundImages/image8.jpg'
import image9 from './BackgroundImages/image9.jpg'
import image10 from './BackgroundImages/image10.jpg'
import image11 from './BackgroundImages/image11.jpg'
import image12 from './BackgroundImages/image12.jpg'


//I tried to change the background image, but it would take some time to load and there
//would be an unpleasant white flask between images. Instead I render 12 different divs,
//and set the opacity on one to 1 and the rest to 0. That way, the transitions are instant.
const backgroundImages = [
    image1, image2, image3, image4,
    image5, image6, image7, image8,
    image9, image10, image11, image12]

const backgroundImageStylingArray = backgroundImages.map((image) => ({
    backgroundImage: `url(${image})`,
    opacity: 0,
}));

const backgroundImageTitles = [
    "Fantasy Island",
    "Dawn of Another Day",
    "Secluded",
    "A Time of Change",
    "Frosch Bokeh 2",
    "Benito",
    "Untitled",
    "Sunset 1663",
    "Europe's Best View",
    "Mists of Renfrew",
    "Tree and Morning Mist",
    "If Only We Could Turn Back Time"

]

const backgroundImagePhotographers = [
    "Daniel Cheong",
    "Sky Matthews",
    "Pete Rowbottom",
    "Rachel Brokaw",
    "Axel F",
    "Ria Putzker",
    "Jorge Guadalupe Lizárraga",
    "Junji Aoyama",
    "Fabian Fortmann",
    "Adam Gibbs",
    "Jos Buurmans",
    "Anna Kwa"
]

function LandingPage() {
    const [backgroundImageIndex, setBackgroundImageIndex] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setBackgroundImageIndex((i) => (i + 1) % backgroundImages.length);
        }, 5000);
        return () => clearInterval(interval);
    }, []);

    const backgroundImageTitle = backgroundImageTitles[backgroundImageIndex];
    const backgroundImagePhotographer = backgroundImagePhotographers[backgroundImageIndex];

    return (
        <>
            <div className="landingHeaderDiv">
                <div className="landingLogoAndTextDiv">
                    <img className='landingLogoImageImg' src="https://i.imgur.com/CN01U69.png" alt="glimmr icon" />
                    <img className='landingLogoImg' src="https://i.imgur.com/b9YTbxQ.png" alt="glimmr logo" />
                </div>
                <div className="landingHeaderLoginAndSignUp">
                    <NavLink className='landingHeaderNavLink' exact to={`/log-in`}>
                        <div className="landingLoginDiv">
                            Log In
                        </div>
                    </NavLink>
                    <NavLink className='landingHeaderNavLink' exact to={`/sign-up`}>
                        <div className='landingSignupDiv'>
                            Sign Up </div>
                    </NavLink>
                </div>
                <div className="landingHeaderBackground"></div>
            </div >

            <div>
                {backgroundImageStylingArray.map((backgroundImageStyling, index) => (
                    <div className="landingBackgroundDiv" key={index} style={{ ...backgroundImageStyling, opacity: backgroundImageIndex === index ? 1 : 0 }}>
                        <div className="centralContentDiv">
                            <div className="findYourInspirationText">Find your inspiration.</div>
                            <div className="joinTheCommunityText">Join the Glimmr community, home to tens of tens of photos.</div>
                            <NavLink className='landingNavLink' exact to={`/sign-up`}>
                                <div className='landingStartDiv'>
                                    Sign Up
                                </div>
                            </NavLink>
                        </div>
                        <div className='landingPhotoCredit'>
                            <div className='backgroundImageTitle'>{backgroundImageTitle}</div>
                            <div className='backgroundImagePhotographer'>by {backgroundImagePhotographer}</div>
                        </div>
                    </div>
                ))}
            </div>

            <div className="landingFooterDiv">
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

            </div >
        </>
    )
}

export default LandingPage
