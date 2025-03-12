import { writable } from 'svelte/store';

export const gameStore = writable({
  started: false,
  gameId: null,
  homeTeam: null,
  awayTeam: null,
  homeLineup: [],
  awayLineup: [],
  currentInning: 1,
  isBottom: false, // false for top, true for bottom
  atBats: []
});
