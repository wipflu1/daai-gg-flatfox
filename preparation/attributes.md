# Listing Attributes

| Attribute                | Type       | Description                                            | Usefull |
|--------------------------|------------|--------------------------------------------------------|---------|
| **pk**                   | int        | Unique identifier for the listing.                     |         |
| **slug**                 | string     | Slug for the listing.                                  |         |
| **url**                  | string     | Public URL of the listing.                             |         |
| **short_url**            | string     | Language independent short URL.                        |         |
| **status**               | string     | Status of the listing. On this endpoint always act.    |         |
| **created**              | datetime   | Creation date of the listing.                          |         |
| **offer_type**           | string     | Offer type, RENT or SELL.                              | y       |
| **object_category**     | string     | Category of the listing.                               |         |
| **object_type**         | string     | Type of the listing.                                   |         |
| **ref_property**        | string     | Property reference.                                    |         |
| **ref_house**           | string     | House reference.                                       |         |
| **ref_object**          | string     | Object reference.                                      |         |
| **price_display**       | int        | Displayed price of the listing.                        |         |
| **price_display_type**  | string     | Type of price display.                                 |         |
| **price_unit**          | string     | Unit of the price (e.g., EUR, USD).                    |         |
| **rent_net**            | int        | Net rent amount.                                       |         |
| **rent_charges**        | int        | Rent charges amount.                                   |         |
| **rent_gross**          | int        | Gross rent amount.                                     |         |
| **short_title**         | string     | Short title of the listing.                            |         |
| **public_title**        | string     | Public title of the listing.                           |         |
| **rent_title**          | string     | Rent title for the listing.                            |         |
| **description_title**   | string     | Title for the description of the listing.              |         |
| **description**        | string     | Description of the listing.                            |         |
| **livingspace**         | int        | Living space area in square meters.                    |         |
| **number_of_rooms**     | string     | Number of rooms in the listing.                        |         |
| **floor**                | int        | Floor number of the listing.                           |         |
| **attributes**          | array      | List of attributes.                                    |         |
| **is_furnished**        | bool       | Indicates if the object is furnished.                  |         |
| **is_temporary**        | bool       | Object is available for a limited timeframe only.      |         |
| **is_selling_furniture**| bool       | Indicates if the object has furniture for sale.        |         |
| **street**              | string     | Street address of the listing.                         |         |
| **zipcode**             | int        | Zip code of the listing address.                       |         |
| **city**                | string     | City of the listing address.                           |         |
| **public_address**      | string     | Public address of the listing.                         |         |
| **latitude**            | float      | Latitude of the listing address.                       |         |
| **longitude**           | float      | Longitude of the listing address.                      |         |
| **year_built**          | int        | Year when the property was built.                      |         |
| **moving_date_type**    | string     | Type of moving date (e.g., specific date or flexible). |         |
| **moving_date**         | date       | Moving date for the listing.                           |         |
| **video_url**           | string     | URL for the video of the listing.                      |         |
| **tour_url**            | string     | URL for the virtual tour of the listing.               |         |
| **website_url**        | string     | Website URL for more information about the listing.    |         |
| **cover_image**         | int        | ID of the cover image for the listing.                 | **yes** |
| **images**              | array      | Array of image IDs for the listing.                    | **yes** |
| **documents**           | array      | Array of document IDs related to the listing.          | **yes** |
| **agency**              | object     | Agency details for the listing.                        | **yes** |

