import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";

function HotspotsMap() {
  return (
    <DashboardLayout>
      <div className="leaflet-container">
        <MapContainer center={[33.6844, 73.0479]} zoom={12} scrollWheelZoom={true}>
          <TileLayer
            url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
            attribution='&copy; <a href="https://carto.com/attribution">CARTO</a>'
          />
        </MapContainer>
      </div>
    </DashboardLayout>
  );
}
export default HotspotsMap;
