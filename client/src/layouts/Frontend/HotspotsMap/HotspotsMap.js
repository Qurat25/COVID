import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, CircleMarker, Popup } from "react-leaflet";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import axios from "axios";

function HotspotsMap() {
  const [data, setData] = useState([]);

  // Function to fetch data from Flask API
  const fetchData = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/getAllData");
      const location_data = response.data;
      var filterData = [];

      for (const location of location_data) {
        const latitude = location.latitude;
        const longitude = location.longitude;

        if (latitude === undefined || longitude === undefined) {
          console.log("Latitude or longitude is undefined.");
          // Handle undefined values
        } else {
          filterData.push({
            latitude: latitude,
            longitude: longitude,
            name: location.name,
            _id: location._id.$oid,
          });
        }
      }
      setData(filterData);
      // setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // Using useEffect for single rendering
  useEffect(() => {
    fetchData();
  }, []);

  console.log(data);
  return (
    <DashboardLayout>
      <div className="leaflet-container">
        <MapContainer center={[33.6844, 73.0479]} zoom={12} scrollWheelZoom={true}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
          {data.length > 0 &&
            data.map((item, index) => (
              <CircleMarker
                key={item._id}
                center={[item.latitude, item.longitude]}
                radius={15}
                pathOptions={{ color: "red" }}
              >
                <Popup>
                  <div>
                    <strong>{item.name}</strong>
                  </div>
                </Popup>
              </CircleMarker>
            ))}
        </MapContainer>
      </div>
    </DashboardLayout>
  );
}
export default HotspotsMap;
