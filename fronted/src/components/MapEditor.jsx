import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';

export const MapEditor = () => (
  <MapContainer center={[52.2297, 21.0122]} zoom={13}>
    <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
  </MapContainer>
);
