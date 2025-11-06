
## List of the URLs to use in testing:

/admin/          --> to visit the admin panel

/restaurant/         --> to visit the static HTML Homepage; supported  method = ['GET']

/api/restaurant/menu/       --> to visit all the menu items; supported  methods = ['GET', 'POST']

/api/restaurant/menu/<int:pk>       --> to visit a single menu item; supported  methods = ['GET', 'PUT', 'PATCH', 'DELETE']


/api/restaurant/booking/tables/          --> to visit all the booked tables; supported  methods = ['GET', 'POST']

/api/restaurant/booking/tables/<int:pk>        --> to visit a single booked table; supported  methods = ['GET', 'PUT', 'PATCH', 'DELETE']



## Authentication URLs:

/api/auth/token/login/         --> to Login (get token); supported  method = ['POST']

/api/auth/token/logout/         --> to Logout (destroy token); supported  method = ['POST']

/api/auth/users/         --> to register a new user; supported  method = ['POST']

/api/auth/users/         --> to list users (authenticated); supported  method = ['GET']

/api/auth/users/me/        --> to get current user, update current user, and delete current user; supported  method = ['GET', 'PUT', 'PATCH', 'DELETE']

/api-token-auth/         --> to obtain auth token; supported  method = ['POST']

