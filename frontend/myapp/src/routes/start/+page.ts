import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
  // Fetch teams from your teams API endpoint (adjust path as needed)
  const res = await fetch('/api/teams/');
  if (res.ok) {
    const teams = await res.json();
    return { teams };
  }
  return { teams: [] };
};
