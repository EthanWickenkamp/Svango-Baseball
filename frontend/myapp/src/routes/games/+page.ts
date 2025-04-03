import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    try {
        const res = await fetch('/api/games/');
        if (!res.ok) throw new Error('Failed to fetch games');
        const games = await res.json();

        // 🔥 Group games by day (YYYY-MM-DD format)
        const gamesByDay = games.reduce((days, game) => {
            const gameDay = game.date; // Already in YYYY-MM-DD format
            if (!days[gameDay]) days[gameDay] = [];
            days[gameDay].push(game);
            return days;
        }, {});

        return { gamesByDay };
    } catch (error) {
        console.error("Error loading games:", error);
        return { gamesByDay: {} };
    }
};
