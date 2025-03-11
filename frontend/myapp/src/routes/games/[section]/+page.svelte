<script lang="ts">
  export let data;
  let game = data.game;
  let atBats = data.atBats;

  // Group at-bats by inning
  let atBatsByInning = {};
  atBats.forEach(atBat => {
      if (!atBatsByInning[atBat.inning]) {
          atBatsByInning[atBat.inning] = [];
      }
      atBatsByInning[atBat.inning].push(atBat);
  });

  // Extract unique innings for column headers
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

<h2>At-Bats by Inning</h2>
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
    {#each [...game.home_team.players, ...game.away_team.players] as player}
      <tr>
        <td>{player.name}</td>
        {#each innings as inning}
          <td>
            {#each atBatsByInning[inning] as atBat}
              {#if atBat.player.id === player.id}
                {atBat.result}  <!-- Show result for player's at-bat -->
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
