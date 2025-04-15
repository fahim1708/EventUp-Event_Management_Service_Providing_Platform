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