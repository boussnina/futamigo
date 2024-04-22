import { useState } from "react"

const Menu = ({ currentIndex, setCurrentIndex }) => {
    const navBar = ["Home", "Statistics", "Contact", "About", "Analytics"]

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
                        style={{ fontWeight: currentIndex === index ? 'bold' : 'normal' }}>
                            {item}</li>
                    ))}
                </ul>
            </div>
        </>
    )
}


export default Menu;

