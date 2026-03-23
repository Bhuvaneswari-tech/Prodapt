import {React, useEffect} from "react";

export function PageLoad() {
    useEffect(() => {
        alert("Page loaded");
    },[]); // Empty dependency array ensures this runs only once on mount
    
    return (
        <div>
            <h1>Welcome to React JS UseEffect</h1>
        </div>
    );
}

//useEffect - Hook to perform side effects in functional components
//alert - function to display an alert box with a message
//Empty dependency array - ensures that the effect runs only once when the component mounts
