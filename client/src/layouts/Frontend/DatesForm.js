import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDButton from "components/MDButton";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import React, { useState, useEffect } from "react";
import axios from "axios";
import Select from "react-select";
import makeAnimated from "react-select/animated";

const DatesForm = () => {
  const [selectedDate, setSelectedDate] = useState("");
  const [selectedLocation, setSelectedLocation] = useState([]);
  const [locationTemp, setLocationTemp] = useState([]);
  const [data, setData] = useState([]);
  const [polygonData, setPolygonData] = useState([]);
  const [selectedPolygon, setSelectedPolygon] = useState([]);
  const [polygonTemp, setPolygonTemp] = useState([]);

  // Function to fetch data from Flask API
  const getAllLocations = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/getAllLocations");
      const filteredData = [];
      for (const location of response.data) {
        let data1 = {
          value: location._id.$oid,
          label: location.name,
        };
        filteredData.push(data1);
      }
      setData(filteredData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const getAllPolygons = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/getAllPolygons");
      const filteredData = [];
      for (const location of response.data) {
        let data1 = {
          value: location._id.$oid,
          label: location.name,
        };
        filteredData.push(data1);
      }
      setPolygonData(filteredData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleDateChange = (event) => {
    setSelectedDate(event.target.value);
  };

  const handleLocationChange = (event) => {
    setLocationTemp(event);
    const locations = [];
    for (const i of event) {
      locations.push(i.value);
    }
    setSelectedLocation(locations);
  };

  const handlePolygonChange = (event) => {
    setPolygonTemp(event);
    const locations = [];
    for (const i of event) {
      locations.push(i.value);
    }
    setSelectedPolygon(locations);
  };

  // Function to filter options based on the search query
  const filterLocationOptions = (option, inputValue) => {
    const label = option.label.toString().toLowerCase();
    const query = inputValue.toLowerCase();
    return label.includes(query);
  };

  // Customize the styles for the options
  const optionStyles = {
    option: (provided) => ({
      ...provided,
      color: "black", // Set the color to black
    }),
  };

  // Using useEffect for single rendering
  useEffect(() => {
    getAllLocations();
    getAllPolygons();
  }, []);

  const collectData = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post("http://localhost:5000/api/addDate", {
        date: selectedDate,
        location: selectedLocation,
        polygon: selectedPolygon,
      });
      if (response.status === 200) {
        alert("Data saved");
      }
    } catch (error) {
      console.error("Error submitting data:", error);
    }
  };

  return (
    <DashboardLayout>
      <MDBox>
        <MDTypography>
          <form>
            <label>Date:</label>
            <input type="date" value={selectedDate} onChange={handleDateChange} />
            <label>Location:</label>
            <Select
              id="locations"
              className="multi-select"
              closeMenuOnSelect={false}
              components={makeAnimated()}
              value={locationTemp}
              onChange={handleLocationChange}
              isMulti
              options={data}
              filterOption={filterLocationOptions}
              styles={optionStyles}
            />
            <label>Polygon:</label>
            <Select
              id="polygons"
              className="multi-select"
              closeMenuOnSelect={false}
              components={makeAnimated()}
              value={polygonTemp}
              onChange={handlePolygonChange}
              isMulti
              options={polygonData}
              filterOption={filterLocationOptions}
              styles={optionStyles}
            />
            <MDButton variant="gradient" color="dark" onClick={collectData}>
              Submit
            </MDButton>
          </form>
        </MDTypography>
      </MDBox>
    </DashboardLayout>
  );
};

export default DatesForm;
