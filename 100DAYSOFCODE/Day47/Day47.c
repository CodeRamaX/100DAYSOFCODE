#include <stdio.h>

int main()
{
    int seats = 80, option, tickets;
    while (1)
    {
        printf("\nRailway Ticket Booking System");
        printf("\n1. Book Ticket");
        printf("\n2. Cancel Ticket");
        printf("\n3. Check Available Seats");
        printf("\n4. Exit");
        printf("\nEnter your option: ");
        scanf("%d", &option);

        if (option == 1)
        {
            printf("\nEnter the number of tickets to book: ");
            scanf("%d", &tickets);
            if (tickets > seats)
            {
                printf("\nNot enough seats available.\n");
            }
            else
            {
                seats -= tickets;
                printf("\n%d Ticket(s) booked successfully.\n", tickets);
            }
        }
        else if (option == 2)
        {
            printf("\nEnter the number of tickets to cancel: ");
            scanf("%d", &tickets);
            seats += tickets;
            printf("\n%d Ticket(s) canceled successfully.\n", tickets);
        }
        else if (option == 3)
        {
            printf("\nAvailable Seats: %d\n", seats);
        }
        else if (option == 4)
        {
            printf("\nThank you for using the Railway Ticket Booking System.\n");
            break;
        }
        else
        {
            printf("\nInvalid options!!!\n");
        }
    }
    return 0;
}


