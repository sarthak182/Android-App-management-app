const deleteApp = () => {
  const appid = document.getElementById("deleteappid").value;

  fetch('/deleteapp', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ appid })
  })
    .then(response => response.json())
    .then(result => {
      alert(result.message || result.error);
      if (result.message) {
        // Find and remove the app row with the matching appid
        const rows = document.querySelectorAll('table tbody tr');
        rows.forEach(row => {
          const cells = row.getElementsByTagName('td');
          if (cells[2] && cells[2].textContent === appid) {  // Assuming appid is in the 3rd column
            row.remove();  // Remove the row from the table
          }
        });
      }
    })
    .catch(error => console.error('Error:', error));
};

const submitDevice = () => {
    const devdata = {
      device_id: document.getElementById("device_id").value,
      device_model: document.getElementById("device_model").value,
      os_version: document.getElementById("os_version").value,
      memory: document.getElementById("memory").value,
      linked_app_id: parseInt(document.getElementById("linked_app_id").value)
    };
  
    fetch('/submitdeviceinfo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(devdata)
    })
      .then(response => response.json())
      .then(result => alert(result.message))
      .catch(error => console.error('Error:', error));
  };
  

const handleClick = () => {
    const appdata = {
      appname: document.getElementById("appname").value,
      appid: document.getElementById("appid").value,
      appfeatures: document.getElementById("appfeatures").value,
    };
  
    fetch("/submitappinfo", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(appdata),
    })
      .then((response) => response.json())
      .then((result) => {
        alert(result.message);
        addRowToTable(appdata);
        // Clear inputs
        document.getElementById("appname").value = "";
        document.getElementById("appid").value = "";
        document.getElementById("appfeatures").value = "";
      })
      .catch((error) => console.error("Error:", error));
  };
  
  function addRowToTable(data) {
    const tableBody = document.querySelector("table tbody");
    const newRow = tableBody.insertRow();
  
    // Note: ID is not returned by backend here, so just use a dash or leave blank
    newRow.insertCell(0).innerText = "-";
    newRow.insertCell(1).innerText = data.appname;
    newRow.insertCell(2).innerText = data.appid;
    newRow.insertCell(3).innerText = data.appfeatures;
  }
  