// export function Increment() {
//     let count = 0;  //state

//     const handleIncrement = () => {
//         count++;
//         console.log(count);
//     };
    
//     return (
//         <div>
//             <h1>Count: {count}</h1>
//             <button onClick={handleIncrement}>Increment</button>
//         </div>
//     );
// }
import { React, useState } from "react";
export function Increment() {
    const [count, setCount] = useState(0);  //state

    const handleIncrement = () => {
        setCount(count + 1);
        console.log(count + 1);
    };
    
    return (
        <div>
            <h1>Count: {count}</h1>
            <button onClick={handleIncrement}>Increment</button>
        </div>
    );
}

//useState - Hook to manage state in functional components

//count - variable to keep track of the count
//handleIncrement - function to increment the count and log it to the console 
// handleIncrement - Event handler for the button click event
//onClick - event handler for the button click event