console.log("Dashboard loaded");

const scanData = {
  ssid: "TestNetwork",
  mac_address: "AA:BB:CC:DD:EE:FF",
  vendor: "Unknown"
};

fetch("http://192.168.1.118:8002", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(scanData)
})
.then(response => response.json())
.then(data => {
  console.log("Response from server:", data);
  const feed = document.getElementById("feed");
  const html = `
    <p>
      <strong>SSID:</strong> ${scanData.ssid}<br>
      <strong>MAC Address:</strong> ${scanData.mac_address}<br>
      <strong>Vendor:</strong> ${scanData.vendor}<br>
      <strong>Hash:</strong> ${data.hash || "N/A"}
    </p>
  `;
  feed.innerHTML += html;
})
.catch(error => {
  console.error("Error:", error);
});
