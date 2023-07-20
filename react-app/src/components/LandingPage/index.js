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

const backgroundImages = [
    image1, image2, image3, image4,
    image5, image6, image7, image8,
    image9, image10, image11, image12]

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
    "Jorge Guadalupe",
    "Junji Aoyama",
    "Fabian Fortmann",
    "Adam Gibbs",
    "Joe Buurmans",
    "Anna Kwa"
]

function LandingPage() {
    const [backgroundImageIndex, setBackgroundImageIndex] = useState(0);

    useEffect(() => {
        setBackgroundImageIndex(Math.floor(Math.random() * backgroundImages.length));
    }, []);

    const backgroundImageStyling = {
        backgroundImage: `url(${backgroundImages[backgroundImageIndex]})`,
    };

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
            <div className="landingBackgroundDiv" style={backgroundImageStyling}>
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
        </>
    )
}

export default LandingPage
