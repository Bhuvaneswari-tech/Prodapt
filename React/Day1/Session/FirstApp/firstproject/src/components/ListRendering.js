const ListRendering = ({ items }) => {
    return (
        <ul>
            {items.map((item, index) => (
                <li key={index}>{item}</li>
            ))}
        </ul>
    );
}

export default ListRendering;

//const items = ['Apple', 'Banana', 'Cherry'];

//ListRendering - name of the component
//items - prop passed to the component
//map() - method used to iterate over the items array and render each item as a list element
//key - unique identifier for each list item (using index in this case)