//Spread Operator
import React from 'react'
//const Spread = ({name, age, city}) => {

const Spread = ({...props}) => {
    return (
        <div>
            <h1>Spread Operator Example</h1>
            <p>Name: {props.name}</p>
            <p>Age: {props.age}</p>
            <p>City: {props.city}</p>
        </div>
    );
}

export default Spread;

//Spread Operator - allows an iterable such as an array or object to be expanded 
// in places where zero or more arguments (for function calls) or elements 
// (for array literals) or key-value pairs (for object literals) are expected. 
// In this example, it is used to pass all props to the component.