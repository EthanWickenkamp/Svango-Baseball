import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
    try {
        // Fetch game details
        const gameRes = await fetch(`/api/games/${params.section}/`);
        if (!gameRes.ok) throw new Error('Game not found');
        const game = await gameRes.json();

        // Fetch at-bats for this game
        const atBatsRes = await fetch(`/api/atbats/?game=${params.section}`);
        let atBats = [];
        if (atBatsRes.ok) {
            atBats = await atBatsRes.json();
        }

        return { game, atBats };
    } catch (error) {
        console.error("Error loading game:", error);
        return { game: null, atBats: [] };
    }
};
