//useRef - focus on input element
import React, { useRef } from 'react';

const FocusInput = () => {
    const inputRef = useRef(null);

    const handleFocus = () => {
        inputRef.current.focus();
    }
    
    return (
        <div>
            <input ref={inputRef} type="text" placeholder="Focus on me!" />
            <button onClick={handleFocus}>Focus Input</button>
        </div>
    );
}

export default FocusInput;

//useRef - Hook to create a reference to a DOM element or a value that persists 
// across renders

//inputRef - reference to the input element

//handleFocus - function to focus the input element when the button is clicked
//onClick - event handler for the button click event