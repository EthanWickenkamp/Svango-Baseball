<script lang="ts">
  export let data: { 
    game: { 
      id: number;
      home_team: { id: number; name: string };
      away_team: { id: number; name: string };
      date: string;
      home_team_score: number;
      away_team_score: number;
    };
  };
</script>

<h1>Game {data.game.id}</h1>

<p><strong>Date:</strong> {data.game.date}</p>

<h2>Teams</h2>
<p><strong>Home:</strong> {data.game.home_team.name}</p>
<p><strong>Away:</strong> {data.game.away_team.name}</p>

<h2>Score</h2>
<p>{data.game.home_team.name}: {data.game.home_team_score}</p>
<p>{data.game.away_team.name}: {data.game.away_team_score}</p>
