import React, { useState } from "react";
import axios from "axios";

function App() {
  const [sensorId, setSensorId] = useState("");
  const [data, setData] = useState(null);

  const fetchData = async () => {
    if (!sensorId) return;

    try {
      const response = await axios.get(
        `http://127.0.0.1:8090/sensor-data/${sensorId}`
      );
      setData(response.data);
    } catch (error) {
      console.error("Error:", error);
      alert("Sensor not found!. Try Again");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Fetch Sensor Data</h2>

      <input
        type="text"
        placeholder="Enter Sensor ID (sensor_404)"
        value={sensorId}
        onChange={(e) => setSensorId(e.target.value)}
        style={{ padding: "8px", marginRight: "10px" }}
      />

      <button onClick={fetchData}>Get Sensor Data</button>

      {data && (
        <table border="1" cellPadding="10" style={{ marginTop: "20px" }}>
          <thead>
            <tr>
              <th>Sensor ID</th>
              <th>Timestamp</th>
              <th>PM2.5</th>
              <th>PM10</th>
              <th>Temperature</th>
              <th>Humidity</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{data.sensor_id}</td>
              <td>{data.timestamp}</td>
              <td>{data.pm25}</td>
              <td>{data.pm10}</td>
              <td>{data.temperature}</td>
              <td>{data.humidity}</td>
            </tr>
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
