document.addEventListener('DOMContentLoaded', () => {
    // Infinite Auto-Scroll JavaScript
    // Function to make the images scroll infinitely
    function autoScroll() {
        const imageSection = document.getElementById('image-section');
        let scrollSpeed = 1; // Speed of the scroll (adjust as needed)

        // Set up the scroll behavior
        function startScroll() {
            imageSection.scrollLeft += scrollSpeed;
            // If we've scrolled to the end, reset to the beginning
            if (imageSection.scrollLeft >= imageSection.scrollWidth - imageSection.clientWidth) {
                imageSection.scrollLeft = 0;
            }
        }

        // Call the startScroll function at a set interval to create the scrolling effect
        setInterval(startScroll, 10); // Adjust the interval for a smoother or faster scroll
    }

    // Initialize the auto-scroll on page load
    window.onload = function() {
        autoScroll();  // Enable infinite auto-scroll
    };

    // JavaScript function for start selling button
    document.getElementById('start-selling-btn')
    .addEventListener('click', () => {
        var confirmation_msg = confirm('You need to log in to start selling!');
        if (confirmation_msg === true) {
            window.location.href ='login';
        }
    }
);

});
