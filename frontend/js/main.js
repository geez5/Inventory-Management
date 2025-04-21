function fetchProduct() {
  const product = document.getElementById("productInput").value;
  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = "";

  fetch(`http://127.0.0.1:5000/api/product/${product}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Product not found.");
      }
      return response.json();
    })
    .then((data) => {
      resultDiv.innerHTML = `
        <strong>Product:</strong> ${data.name}<br/>
        <strong>Quantity:</strong> ${data.quantity}<br/>
        <strong>Sold Last Month:</strong> ${data.sold_last_month}<br/>
        <strong>Estimated Days Until Empty:</strong> ${data.estimated_days_until_empty}<br/>
        <strong>Expiring Soon:</strong> ${data.expiring_soon ? "✅ Yes" : "❌ No"}<br/>
        <strong>Needs Restock:</strong> ${data.needs_restock ? "⚠️ Yes" : "✅ No"}<br/>
        <strong>Suggested Quantity to Buy:</strong> ${data.suggested_quantity}
      `;
    })
    .catch((error) => {
      resultDiv.innerHTML = `<div class="error">❌ ${error.message}</div>`;
    });
}