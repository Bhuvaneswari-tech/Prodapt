const ConditionalRendering = ({ isLoggedIn }) => {
    return (
        <div>
            {isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign in.</h1>}
        </div>
    );
};

export default ConditionalRendering;

//isLoggedIn - prop passed to the component
//Conditional rendering - rendering different elements based on a condition
//Ternary operator - condition ? true : false