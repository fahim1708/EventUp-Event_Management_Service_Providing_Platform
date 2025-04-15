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

    incrementButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            let currentQuantity = parseInt(quantityDisplays[index].textContent, 10);
            currentQuantity++;
            quantityDisplays[index].textContent = currentQuantity;
        });
    });

    decrementButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            let currentQuantity = parseInt(quantityDisplays[index].textContent, 10);
            if (currentQuantity > 0) {
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
                }

                // Store selected items and quantities in localStorage
                localStorage.setItem('selectedItemsQuantity', JSON.stringify(selectedItemsQuantity));
                localStorage.setItem('selectedItems', JSON.stringify(selectedItems));
            } else {
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

        // Redirect to the confirmation page with the selected item IDs and quantities
        const queryString = `selectedItems=${items.join(',')}&itemsWithQuantity=${encodeURIComponent(JSON.stringify(itemsWithQuantity))}`;
        window.location.href = `/confirmation/?${queryString}`;
    });

    document.querySelector('#confirmationButton2').addEventListener('click', function() {
        // Retrieve selected items and quantities from localStorage
        const items = JSON.parse(localStorage.getItem('selectedItems'));
        const itemsWithQuantity = JSON.parse(localStorage.getItem('selectedItemsQuantity'));

        // Redirect to the confirmation page with the selected item IDs and quantities
        const queryString = `selectedItems=${items.join(',')}&itemsWithQuantity=${encodeURIComponent(JSON.stringify(itemsWithQuantity))}`;
        window.location.href = `/confirmation/?${queryString}`;
    });
    // Package and Item Selection End

    
    // Disabling the quantity increment and decrement button Start
    // Retrieve all select buttons
    const selectButtons = document.querySelectorAll(".item-selection");
    // Loop over each select button
    selectButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const itemId = button.getAttribute("data-item-id");

            // Disable the increment and decrement buttons after selecting
            const decrementButton = button.closest(".rectangle-parent17").querySelector(".decrement-button");
            const incrementButton = button.closest(".rectangle-parent17").querySelector(".increment-button");

            // Disable the buttons
            decrementButton.style.pointerEvents = "none";
            decrementButton.style.opacity = "0.5";
            incrementButton.style.pointerEvents = "none";
            incrementButton.style.opacity = "0.5";

            // Optionally, change the text of the select button to "Selected"
            button.querySelector('.select9').innerText = "Selected";
        });
    });
    // Disabling the quantity increment and decrement button End
});


