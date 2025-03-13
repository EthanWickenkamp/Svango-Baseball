import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
    const gameId = params.live; // Extract the game ID from the URL

    const response = await fetch(`/api/games/${gameId}/`);
    if (!response.ok) {
        return { status: response.status, error: new Error("Game not found") };
    }

    const game = await response.json();
    return { game };
};
