/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        // to match bootstrap alert class
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submission
let form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    // Prevent multiple submissions after event has been called
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-screen').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            // Show error message to customer
            let errorDiv = document.getElementById('card-errors');
            let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-screen').fadeToggle(100);
            // Re-enable card to allow error to be fixed
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // Show success message to customer
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});