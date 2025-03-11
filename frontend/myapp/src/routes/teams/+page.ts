import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    try {
        // Fetch teams (players inside teams only)
        const teamRes = await fetch('/api/teams/');
        if (!teamRes.ok) throw new Error('Failed to fetch teams');
        const teams = await teamRes.json();

        // Fetch free agents separately (players with no team)
        const freeAgentRes = await fetch('/api/players/?team=null');
        let freeAgents = [];
        if (freeAgentRes.ok) {
            freeAgents = await freeAgentRes.json();
        }

        return { teams, freeAgents };
    } catch (error) {
        console.error("Error loading data:", error);
        return { teams: [], freeAgents: [] }; // Prevent crash
    }
};
