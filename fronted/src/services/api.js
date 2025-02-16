import axios from 'axios';

export const fetchMPZP = (coordinates) => 
  axios.post('/api/plots/check-mpzp/', { coordinates });
