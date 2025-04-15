document.addEventListener('DOMContentLoaded', function() {

    // Package  & Item Scroll Start
    var homeContainer = document.getElementById("packageName");
    if (homeContainer) {
        homeContainer.addEventListener("click", function () {
            var anchor = document.querySelector("[data-scroll-to='ourPackageContent']");
            if (anchor) {
        anchor.scrollIntoView({ block: "start", behavior: "smooth" });
        }
    });
    }
    var itemName = document.getElementById("itemName");
    if (itemName) {
    itemName.addEventListener("click", function () {
        var anchor = document.querySelector("[data-scroll-to='ourItemContent']");
        if (anchor) {
        anchor.scrollIntoView({ block: "start", behavior: "smooth" });
        }
    });
    }
    // Package  & Item Scroll End


    // Quantity displays, increment and decrement buttons start
    const quantityDisplays = document.querySelectorAll('.quantity-display');
    const incrementButtons = document.querySelectorAll('.increment-button');
    const decrementButtons = document.querySelectorAll('.decrement-button');
    const availableDiv = document.querySelectorAll('.available-5-pices3');

    incrementButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            const avl_element = availableDiv[index];
            const availableQuantity = avl_element.dataset.ablQuantity;
            
            let currentQuantity = parseInt(quantityDisplays[index].textContent, 10);

            if (currentQuantity < availableQuantity) {
                currentQuantity++;
                quantityDisplays[index].textContent = currentQuantity;
            }
        });
    });

    decrementButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            let currentQuantity = parseInt(quantityDisplays[index].textContent, 10);
            if (currentQuantity > 1) {
                currentQuantity--;
            }
            quantityDisplays[index].textContent = currentQuantity;
        });
    });
    // Quantity displays, increment and decrement buttons End


    // Package and Item Selection Start
    let selectedItems = [];
    const selectedItemsQuantity = {}; // Object to store selected item IDs with quantities

    // Handle the selection of an item
    document.querySelectorAll('.item-selection').forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.dataset.itemId; // Get the itemId from the data attribute
            const itemIndex = selectedItems.indexOf(itemId);
            const parentElement = this.closest('.rectangle-parent17');
            
            // Disable the increment and decrement buttons after selecting
            const decrementButton = parentElement.querySelector(".decrement-button");
            const incrementButton = parentElement.querySelector(".increment-button");

            // Check if the item has a quantity display
            const quantityDisplay = document.getElementById(`quantityDisplay${itemId}`);
            if (quantityDisplay) {
                const selectedQuantity = parseInt(quantityDisplay.textContent);

                // Toggle selection and store the quantity if the item is selected
                if (selectedItemsQuantity[itemId]) {
                    delete selectedItemsQuantity[itemId]; // Deselect and remove from quantity tracking
                    if (itemIndex !== -1) {
                        selectedItems.splice(itemIndex, 1);
                    }
                    this.querySelector('.select9').innerText = 'Select';
                    this.querySelector('.select9').style.color = 'var(--color-blueviolet-100)';
                    parentElement.style.backgroundColor = 'white';
                    this.style.backgroundColor = 'white';
                    // Deselect the item: enable the buttons and change the text back to "Select"
                    decrementButton.style.pointerEvents = "auto";
                    decrementButton.style.opacity = "1";
                    incrementButton.style.pointerEvents = "auto";
                    incrementButton.style.opacity = "1";
                    }
                else {
                    selectedItemsQuantity[itemId] = selectedQuantity; // Store item with quantity
                    if (itemIndex === -1) {
                        selectedItems.push(itemId);
                    }
                    this.querySelector('.select9').innerText = 'Selected';
                    this.querySelector('.select9').style.color = 'white';
                    this.style.backgroundColor = 'var(--color-blueviolet-100)';
                    parentElement.style.backgroundColor = 'rgb(220 207 255)';
                    // Disable the buttons
                    decrementButton.style.pointerEvents = "none";
                    decrementButton.style.opacity = "0.5";
                    incrementButton.style.pointerEvents = "none";
                    incrementButton.style.opacity = "0.5";
                }

                // Store selected items and quantities in localStorage
                localStorage.setItem('selectedItemsQuantity', JSON.stringify(selectedItemsQuantity));
                localStorage.setItem('selectedItems', JSON.stringify(selectedItems));
            } 
            else {
                // Handle case where there's no quantity display (old logic)
                if (itemIndex === -1) {
                    selectedItems.push(itemId);
                    this.querySelector('.select9').innerText = 'Selected';
                    this.querySelector('.select9').style.color = 'white';
                    this.style.backgroundColor = 'var(--color-blueviolet-100)';
                    parentElement.style.backgroundColor = 'rgb(220 207 255)';
                } else {
                    selectedItems.splice(itemIndex, 1);
                    this.querySelector('.select9').innerText = 'Select';
                    this.querySelector('.select9').style.color = 'var(--color-blueviolet-100)';
                    parentElement.style.backgroundColor = 'white';
                    this.style.backgroundColor = 'white';
                }

                // Store selected items in localStorage (without quantity)
                localStorage.setItem('selectedItems', JSON.stringify(selectedItems));
            }
        });
    });



    // Send selected items and quantities when navigating to the next page
    document.querySelector('#confirmationButton').addEventListener('click', function() {
        // Retrieve selected items and quantities from localStorage
        const items = JSON.parse(localStorage.getItem('selectedItems'));
        const itemsWithQuantity = JSON.parse(localStorage.getItem('selectedItemsQuantity'));

        const startDate = document.querySelector('#start_date').value;
        const endDate = document.querySelector('#end_date').value;

        // Redirect to the confirmation page with the selected item IDs and quantities
        // const queryString = `selectedItems=${items.join(',')}&itemsWithQuantity=${encodeURIComponent(JSON.stringify(itemsWithQuantity))}`;
        const queryString = `selectedItems=${items.join(',')}&itemsWithQuantity=${encodeURIComponent(JSON.stringify(itemsWithQuantity))}&start_date=${encodeURIComponent(startDate)}&end_date=${encodeURIComponent(endDate)}`;
        window.location.href = `/confirmation/?${queryString}`;
    });
    
    document.querySelector('#confirmationButton2').addEventListener('click', function() {
        // Retrieve selected items and quantities from localStorage
        const items = JSON.parse(localStorage.getItem('selectedItems'));
        const itemsWithQuantity = JSON.parse(localStorage.getItem('selectedItemsQuantity'));
        
        const startDate = document.querySelector('#start_date').value;
        const endDate = document.querySelector('#end_date').value;

        // Redirect to the confirmation page with the selected item IDs and quantities
        //const queryString = `selectedItems=${items.join(',')}&itemsWithQuantity=${encodeURIComponent(JSON.stringify(itemsWithQuantity))}`;
        const queryString = `selectedItems=${items.join(',')}&itemsWithQuantity=${encodeURIComponent(JSON.stringify(itemsWithQuantity))}&start_date=${encodeURIComponent(startDate)}&end_date=${encodeURIComponent(endDate)}`;
        window.location.href = `/confirmation/?${queryString}`;
    });
    // Package and Item Selection End
});

window.addEventListener('beforeunload', function() {
    localStorage.removeItem('selectedItems');
    localStorage.setItem('selectedItemsQuantity', JSON.stringify({}));
});

// pop_up message loader Start
// Function to show the pop-up and make it disappear after a few seconds
function showPopup() {
const popup = document.getElementById("popup");
popup.classList.add("show-popup");

// Hide the pop-up after 3 seconds
setTimeout(() => {
    popup.classList.remove("show-popup");
}, 3000);
}

// Trigger the pop-up when the page loads (optional)
window.onload = showPopup;


