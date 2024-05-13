import { useState } from "react"

const Menu = ({ currentIndex, setCurrentIndex }) => {
    const navBar = ["Home", "Statistics", "Analytics", "Win probabilities", "Futl", "About"]

    const handleClick = (index) => {
        setCurrentIndex(index)
    }

    return (
        <>
            <div className="menu-container">
                <ul>
                {navBar.map((item, index) => (
                    <li 
                        key={index} 
                        onClick={() => handleClick(index)}
                        className={currentIndex === index ? 'chosen' : ''}>
                        {item}
                    </li>
                    ))}
                </ul>
            </div>
        </>
    )
}


export default Menu;

