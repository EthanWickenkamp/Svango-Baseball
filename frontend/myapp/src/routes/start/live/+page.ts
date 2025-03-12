import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params, fetch }) => {
  const res = await fetch(`/api/games/live/${params.live}/`);
  if (res.ok) {
    const game = await res.json();
    return { game };
  }
  throw new Error("Could not load game information.");
};
