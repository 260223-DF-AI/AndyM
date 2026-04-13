select h.hacker_id, h.name, count(*) as num_full_scores
FROM Hackers h JOIN Submissions s ON h.hacker_id = s.hacker_id
JOIN Challenges c on s.challenge_id = c.challenge_id
JOIN Difficulty d on d.difficulty_level = c.difficulty_level
WHERE s.score = d.score
GROUP BY h.hacker_id
HAVING num_full_scores > 1
ORDER BY num_full_scores desc h.hacker_id asc;
