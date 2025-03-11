import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    try {
        // Fetch teams (players inside teams)
        const teamRes = await fetch('/api/teams/');
        if (!teamRes.ok) throw new Error('Failed to fetch teams');
        const teams = await teamRes.json();

        // Fetch free agents separately
        const freeAgentRes = await fetch('/api/players/?team=null');
        let freeAgents = [];
        if (freeAgentRes.ok) {
            freeAgents = await freeAgentRes.json();
        }

        // ✅ Ensure only actual free agents are assigned
        //freeAgents = freeAgents.filter(player => player.team === null);

        return { teams, freeAgents };
    } catch (error) {
        console.error("Error loading data:", error);
        return { teams: [], freeAgents: [] }; // Prevent crash
    }
};
