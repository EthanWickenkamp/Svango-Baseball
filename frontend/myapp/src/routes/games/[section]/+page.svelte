<script lang="ts">
  export let data;
  let game = data.game;
  let gameStats = data.game.gamestats;

  // Ensure gameStats exist
  if (!gameStats) {
    console.error("GameStats is missing from API response");
  }

  // Group at-bats by inning and team
  let atBatsByInning = {};

  gameStats.forEach(stat => {
    stat.atbats.forEach(atBat => {
      if (!atBatsByInning[atBat.inning]) {
        atBatsByInning[atBat.inning] = { home: [], away: [] };
      }

      // Sort at-bats based on player's team
      if (stat.team === game.home_team.name) {
        atBatsByInning[atBat.inning].home.push({ player: stat.player.name, result: atBat.outcome });
      } else {
        atBatsByInning[atBat.inning].away.push({ player: stat.player.name, result: atBat.outcome });
      }
    });
  });

  // Extract unique innings for table headers
  let innings = Object.keys(atBatsByInning).map(Number).sort((a, b) => a - b);
</script>

<h1>Game Details</h1>
<p>Date: {new Date(game.game_date).toLocaleDateString()}</p>

<h2>Teams & Score</h2>
<p>
  <strong>{game.home_team.name}</strong> 
  <span class="game-score">{game.home_team_score} - {game.away_team_score}</span>
  <strong>{game.away_team.name}</strong>
</p>

<h2>{game.home_team.name} - At-Bats by Inning</h2>
<table>
  <thead>
    <tr>
      <th>Player</th>
      {#each innings as inning}
        <th>Inning {inning}</th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each gameStats.filter(stat => stat.team === game.home_team.name) as stat}
      <tr>
        <td>{stat.player.name}</td>
        {#each innings as inning}
          <td>
            {#each atBatsByInning[inning]?.home as atBat}
              {#if atBat.player === stat.player.name}
                {atBat.result.replace("_", " ")}
              {/if}
            {/each}
          </td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table>

<h2>{game.away_team.name} - At-Bats by Inning</h2>
<table>
  <thead>
    <tr>
      <th>Player</th>
      {#each innings as inning}
        <th>Inning {inning}</th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each gameStats.filter(stat => stat.team === game.away_team.name) as stat}
      <tr>
        <td>{stat.player.name}</td>
        {#each innings as inning}
          <td>
            {#each atBatsByInning[inning]?.away as atBat}
              {#if atBat.player === stat.player.name}
                {atBat.result.replace("_", " ")}
              {/if}
            {/each}
          </td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table>

<button on:click={() => history.back()}>Back</button>

<style>
  h1, h2 {
    color: #0077cc;
  }

  .game-score {
    font-weight: bold;
    font-size: 1.5em;
    color: #0077cc;
    margin: 0 10px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th, td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
  }

  th {
    background-color: #f4f4f4;
    font-weight: bold;
  }

  button {
    background-color: #0077cc;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    font-size: 1em;
    border-radius: 5px;
    margin-top: 20px;
  }

  button:hover {
    background-color: #005fa3;
  }
</style>
