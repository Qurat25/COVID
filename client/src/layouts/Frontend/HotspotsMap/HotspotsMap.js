import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";

function HotspotsMap() {
  return (
    <DashboardLayout>
      <div className="leaflet-container">
        <MapContainer center={[33.6844, 73.0479]} zoom={12} scrollWheelZoom={true}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
        </MapContainer>
      </div>
    </DashboardLayout>
  );
}
export default HotspotsMap;
