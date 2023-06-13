def find_winner(candidates):
    vote_count = {}

    # Count the votes for each candidate
    for candidate in candidates:
        vote_count[candidate] = vote_count.get(candidate, 0) + 1

    # Find the maximum vote count
    max_votes = max(vote_count.values())

    # Retrieve the candidate(s) with maximum votes
    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]

    # Sort the winners lexicographically
    winners.sort()

    return winners


# Example usage
votes = ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Bob', 'Charlie']
result = find_winner(votes)
print("Candidates with maximum votes (in lexicographical order):")
print(result)
