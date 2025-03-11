<script lang="ts">
  import { goto } from '$app/navigation';

  export let data;
  let gamesByDay = data.gamesByDay;

  // Convert object to an array of [date, games] and sort by date
  let sortedGames = Object.entries(gamesByDay)
    .map(([date, games]) => [new Date(date), games])
    .sort((a, b) => a[0].getTime() - b[0].getTime()); // Sort in ascending order

  function viewGame(gameId: string) {
    goto(`/games/${gameId}/`);
  }
</script>

<h1>Game Results by Day</h1>

{#if sortedGames.length === 0}
  <p>No games available.</p>
{:else}
  {#each sortedGames as [gameDate, games]}
    <div class="game-day">
      <h2>{gameDate.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' })}</h2>
      <ul>
        {#each games as game}
          <li>
            <button class="view-game-btn" on:click={() => viewGame(game.id)} aria-label="View game details">
              View Game
            </button>

            <span class="team-name">{game.home_team.name}</span>
            <span class="score">
              <span class="{game.home_team_score > game.away_team_score ? 'winner-score' : 'loser-score'}">
                {game.home_team_score}
              </span>
              -
              <span class="{game.away_team_score > game.home_team_score ? 'winner-score' : 'loser-score'}">
                {game.away_team_score}
              </span>
            </span>
            <span class="team-name">{game.away_team.name}</span>
          </li>
        {/each}
      </ul>
    </div>
  {/each}
{/if}

<style>
  /* General Styling */
  h1 {
    text-align: center;
    font-size: 2em;
    color: #222;
  }

  .game-day {
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f8f9fa;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  }

  h2 {
    font-size: 1.5em;
    color: #0077cc;
    margin-bottom: 10px;
  }

  /* Button Styling */
  .view-game-btn {
    background-color: #0077cc;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    font-size: 1em;
    border-radius: 5px;
    margin-right: 10px;
    transition: background 0.3s ease-in-out;
  }

  .view-game-btn:hover {
    background-color: #005fa3;
  }

  /* List Styling */
  ul {
    list-style: none;
    padding: 0;
  }

  li {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 15px;
    font-size: 1.2em;
    padding: 10px 0;
    border-bottom: 1px solid #ddd;
  }

  li:last-child {
    border-bottom: none;
  }

  /* Score and Team Name Styling */
  .team-name {
    font-size: 1.3em;
    font-weight: bold;
    color: #222;
    margin: 0 10px;
  }

  .score {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 1.4em;
  }

  .winner-score {
    color: #0077cc;
    font-weight: bold;
    font-size: 1.5em;
  }

  .loser-score {
    color: #555;
    font-weight: normal;
    font-size: 1.2em;
  }
</style>
