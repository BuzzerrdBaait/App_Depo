// Function to process and print the input value
const processInput = (value) => {
     console.log("You entered: " + value);
 
     // Clear the input box after printing the value
     const inputElement = document.getElementById("e1");
     inputElement.value = '';
 };
 
 // Add a click event listener to the search button
 const searchButton = document.getElementById("searchButton");
 searchButton.addEventListener("click", () => {
     const inputElement = document.getElementByClass("flexbox-item flexbox-item-entrybox");
     const inputValue = inputElement.value;
     processInput(inputValue);
 });
 
 // Add an event listener for Enter key press to trigger search
 const inputElement = document.getElementByClass("flexbox-item flexbox-item-entrybox");
 inputElement.addEventListener("keypress", (event) => {
     if (event.key === 'Enter') {
         const inputValue = inputElement.value;
         processInput(inputValue);
     }
 });