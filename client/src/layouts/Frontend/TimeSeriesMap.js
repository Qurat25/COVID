import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import axios from "axios";

function TimeSeriesMap() {
  const [data, setData] = useState([]);
  const [selectedDate, setSelectedDate] = useState(""); // State to store selected date
  const [sliderValue, setSliderValue] = useState(0);
  const [locationData, setLocationData] = useState([]);
  const Icon = L.icon({
    iconUrl: "https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png",
    shadowUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
  });

  // Function to fetch data from Flask API
  const getAllDates = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/getAllDates");
      setData(response.data); // Update the dates state with fetched data
      if (response.data.length > 0) {
        setSelectedDate(response.data[0].date); // Set default selected date
      }
      // setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const getLocationByDate = async (filterDate) => {
    try {
      const response = await axios.get("http://localhost:5000/api/getLocationByDate", {
        params: { filterDate: filterDate },
      });
      const location_data = response.data[0].populated_location;
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
      setLocationData(filterData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleDateChange = (event) => {
    const selectedIndex = parseInt(event.target.value, 10);
    setSliderValue(selectedIndex);
    setSelectedDate(data[selectedIndex]?.date);
    getLocationByDate(data[selectedIndex]?.date);
  };

  // Using useEffect for single rendering
  useEffect(() => {
    getAllDates();
    getLocationByDate("2020-05-03");
  }, []);

  return (
    <DashboardLayout>
      <div className="slider-container">
        <input
          type="range"
          min="0"
          max={data.length - 1}
          value={sliderValue}
          onChange={handleDateChange}
          list="dateOptions"
        />
        <datalist id="dateOptions">
          {data.map((item, index) => (
            <option key={index} value={index} label={item.date} />
          ))}
        </datalist>
        <p>Selected Date: {selectedDate}</p>
      </div>
      <div className="leaflet-container">
        <MapContainer center={[33.5844, 73.0479]} zoom={11} scrollWheelZoom={true}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
          {locationData.length > 0 &&
            locationData.map((item, index) => (
              <Marker key={item._id} position={[item.latitude, item.longitude]} icon={Icon}>
                <Popup>
                  <div>
                    <strong>{item.name}</strong>
                  </div>
                </Popup>
              </Marker>
            ))}
        </MapContainer>
      </div>
    </DashboardLayout>
  );
}
export default TimeSeriesMap;
