def time_required_to_buy(tickets: list[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    from collections import deque
    queue = deque(tickets)
    time = 0
    while queue[k] > 0:
        length = len(queue)
        while length > 0:
            current_person_tickets = queue.popleft()
            remaining_tickets = current_person_tickets - 1 if (current_person_tickets - 1) > 0 else 0
            queue.append(remaining_tickets)
            k = (k - 1)%len(queue)
            time = time + 1 if current_person_tickets > 0 else time
            length -= 1
            if queue[k] == 0:
                return time
    
    return time

if __name__ == "__main__":
    tickets = [int(x) for x in input().split()]
    k = int(input())
    res = time_required_to_buy(tickets, k)
    print(res)
