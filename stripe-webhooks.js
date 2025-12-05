/**
 * FISH MUSIC INC - Stripe Webhook Handler
 * Automated payment processing and notifications
 */

const express = require("express");
const router = express.Router();

// Stripe webhook endpoint
router.post(
  "/stripe",
  express.raw({ type: "application/json" }),
  (req, res) => {
    const sig = req.headers["stripe-signature"];
    const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

    let event;

    try {
      // Verify webhook signature (when Stripe is configured)
      if (webhookSecret) {
        const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
        event = stripe.webhooks.constructEvent(req.body, sig, webhookSecret);
      } else {
        event = JSON.parse(req.body);
      }

      console.log("🔔 Stripe webhook received:", event.type);

      // Handle different event types
      switch (event.type) {
        case "payment_intent.succeeded":
          handlePaymentSuccess(event.data.object);
          break;
        case "payment_intent.payment_failed":
          handlePaymentFailure(event.data.object);
          break;
        case "customer.created":
          handleNewCustomer(event.data.object);
          break;
        case "invoice.paid":
          handleInvoicePaid(event.data.object);
          break;
        case "subscription.created":
          handleSubscriptionCreated(event.data.object);
          break;
        default:
          console.log(`Unhandled event type: ${event.type}`);
      }

      res.json({ received: true });
    } catch (err) {
      console.error("❌ Webhook error:", err.message);
      res.status(400).send(`Webhook Error: ${err.message}`);
    }
  }
);

function handlePaymentSuccess(paymentIntent) {
  console.log("✅ Payment succeeded:", paymentIntent.id);
  console.log(
    "   Amount:",
    paymentIntent.amount / 100,
    paymentIntent.currency.toUpperCase()
  );
  console.log("   Customer:", paymentIntent.customer);

  // TODO: Send confirmation email
  // TODO: Update database
  // TODO: Trigger fulfillment
}

function handlePaymentFailure(paymentIntent) {
  console.log("❌ Payment failed:", paymentIntent.id);
  console.log("   Reason:", paymentIntent.last_payment_error?.message);

  // TODO: Send failure notification
  // TODO: Log for follow-up
}

function handleNewCustomer(customer) {
  console.log("👤 New customer:", customer.id);
  console.log("   Email:", customer.email);
  console.log("   Name:", customer.name);

  // TODO: Add to CRM
  // TODO: Send welcome email
}

function handleInvoicePaid(invoice) {
  console.log("💰 Invoice paid:", invoice.id);
  console.log(
    "   Amount:",
    invoice.amount_paid / 100,
    invoice.currency.toUpperCase()
  );

  // TODO: Send receipt
  // TODO: Update accounting
}

function handleSubscriptionCreated(subscription) {
  console.log("📅 Subscription created:", subscription.id);
  console.log("   Customer:", subscription.customer);
  console.log("   Status:", subscription.status);

  // TODO: Provision access
  // TODO: Send welcome email
}

module.exports = router;
