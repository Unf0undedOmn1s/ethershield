// Log to confirm JS is running
console.log("Dashboard loaded");

// Sample scan data to send
const scanData = {
  ssid: "TestNetwork",
  bssid: "AA:BB:CC:DD:EE:FF",
  zone: "Room A"
};

// Send POST request to FastAPI backend
fetch("http://localhost:8000/submit-scan", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(scanData)
})
.then(response => response.json())
.then(data => {
  console.log("Response from server:", data);

  // Update the dashboard
  const feed = document.getElementById("feed");
  const html = `
    <p>
      <strong>SSID:</strong> ${scanData.ssid}<br>
      <strong>BSSID:</strong> ${scanData.bssid}<br>
      <strong>Zone:</strong> ${scanData.zone}<br>
      <strong>Hash:</strong> ${data.hash}
    </p>
  `;
  feed.innerHTML += html;
})
.catch(error => {
  console.error("Error:", error);
});
