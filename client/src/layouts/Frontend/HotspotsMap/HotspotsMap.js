import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, CircleMarker, Popup, Polygon } from "react-leaflet";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import axios from "axios";

function HotspotsMap() {
  const [data, setData] = useState([]);
  const [polygonData, setPolygonData] = useState([]);
  const polygonPositions = [
    [51.505, -0.09],
    [51.51, -0.1],
    [51.51, -0.12],
  ];

  // Function to fetch data from Flask API
  const getAllLocations = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/getAllLocations");
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
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // Function to fetch data from Flask API
  const getAllPolygons = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/getAllPolygons");
      const location_data = response.data;
      var filterData = [];

      for (const location of location_data) {
        filterData.push({
          coordinates: location.coordinates,
          name: location.name,
          _id: location._id.$oid,
        });
      }
      setPolygonData(filterData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // Using useEffect for single rendering
  useEffect(() => {
    getAllLocations();
    getAllPolygons();
  }, []);

  return (
    <DashboardLayout>
      <div className="leaflet-container">
        <MapContainer center={[33.5844, 73.0479]} zoom={11} scrollWheelZoom={true}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
          {polygonData.length > 0 &&
            polygonData.map((item, index) => (
              <Polygon key={item._id} positions={item.coordinates} color="blue">
                <Popup>
                  <div>
                    <strong>{item.name}</strong>
                  </div>
                </Popup>
              </Polygon>
            ))}
          {/* {data.length > 0 &&
            data.map((item, index) => (
              <CircleMarker
                key={item._id}
                center={[item.latitude, item.longitude]}
                radius={10}
                pathOptions={{ color: "red" }}
              >
                <Popup>
                  <div>
                    <strong>{item.name}</strong>
                  </div>
                </Popup>
              </CircleMarker>
            ))} */}
        </MapContainer>
      </div>
    </DashboardLayout>
  );
}
export default HotspotsMap;
