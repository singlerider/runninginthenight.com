---
layout: default
title: netstat
permalink: /netstat/
---

# Staying Connected at Sea

For now, [Starlink](https://www.starlink.com/) is the best way to stay connected at sea.

There are lots of excellent guides and videos by the [Mobile Internet Resource Center](https://www.rvmobileinternet.com/guides/alternatives-to-starlink/), but I will be going over a solution for a particular demographic: The sailor that is "out there," doing "it" — Going into remote places where there's still ambiguity in the world. Let's try and clear some of that up with a small amount of exposition, identifying my use-case:

I am a sailor that is on his way, westbound, around the world, and I work a full-time job. For better or worse, to fund my adventures, I require network connectivity on the order of about 1 terabyte per month. Consider this a living document for how I am *currently* meeting my networking needs.

## The Problem

Starlink seems to gear itself towards stationary or terrestrial customers that tend to stay on the same "continent" or country. What happens when you're, for example, in the Caribbean Islands or the South Pacific, where you could be going through a new country every few days? Starlink does a **bad** job of explaining what will work, where, for how long, and how much it will cost. They'll also change the terms of service on a whim, forcing knee-jerk reactions, with unresponsive customer support staff, leaving you on your own (as I was when I approaching the Marquesas Islands after being at sea for three straight weeks).

Let's look at some service plans:

Starlink [offers their services by region](https://www.starlink.com/us/map). The whole world isn't currently a uniform color on their map. Note that French Polynesia is "Staring in 2026." Well, here's where their confusion pills begin. Let's consider French Polynesia to be part of a larger region/continent. Although Starlink does not claim that service is available in a specific country, that doesn't mean it's actually the case. See [this FAQ from Starlink](https://www.starlink.com/support/article/dd5b43b5-20e1-b29b-2d7d-a7ffd0541988) to explain the "Roam" service plan.

>Countrywide coverage (including inland waterways and marinas) within **country of account address**

The verbiage is not true. Having a New Zealand service plan treats the entirety of Oceania as a "country." That includes the Marquesas Islands to the East and Australia in the West.

Let's look at [some service plans](https://www.starlink.com/service-plans) and their corresponding prices in US Dollars:

<table border="1">
  <tr>
    <th>Name</th><th>Price</th><th><a href="https://www.starlink.com/support/article/50e933eb-54f5-1a77-cc85-c6c8325564cf">In-Motion?</a></th><th><a href="https://www.starlink.com/support/article/09b6cfbe-503a-bacb-6d2d-93222a828b97">Ocean?</a></th>
  </tr>
  <tr>
    <td><a href="https://www.rvmobileinternet.com/guides/starlink-rv-boat/#Roam_Service_Plans">Global Roam</a></td><td>$400</td><td align="center">x</td><td></td>
  </tr>
  <tr>
    <td><a href="https://www.starlink.com/support/article/6e0a6781-d9e6-8cc1-153e-763daa011f9a">Residential</a></td><td>$120</td><td align="center"></td><td></td>
  </tr>
  <tr>
    <td><a href="https://www.starlink.com/support/article/dd5b43b5-20e1-b29b-2d7d-a7ffd0541988">Roam Unlimited</a></td><td>$165</td><td align="center">x</td><td></td>
  </tr>
</table>

The undocumented Global Roam plan will probably do the trick, but it's $400 USD and still doesn't cover "Ocean," and also isn't available to new customers that are just signing up. Residential is only for stationary units that should not expect for continuous network use while moving. Roam Unlimited is still cheaper, but the description makes it seem like it will only work in specific places. No matter which plan you choose, you will be paying high prices for Ocean data at a rate of $2 USD per gigabyte. This type of data is called "Mobile Priority" and can be opted into at any time if your plan supports it on the app, even while you're at sea and have no existing external Internet connection. 

## The Solution(s)

### [Transfer Your Service](https://www.starlink.com/support/article/f3cad923-ed28-f957-365c-787f8fe2e4a2) to Yourself

What we need to do is transfer your service to a more favorable address to a new region that will support your intended use-cases in the remote area that you are in. This will create a new "account" with a new number, that can still be associated with your existing email address. What Starlink refers to as an "account" is just a combination of your email address and an association with a specific address/country.

This process requires cancelling your existing service for every dish you intend on transferring. I did this with two dishes, which was more complicated than with just one, but we'll get you through this if you're *in the same boat*. **These steps are best performed on a desktop machine or on a "Desktop Site"-checked Chrome-like mobile browser window.

1. Cancel your service

    A. From your [Starlink account](https://www.starlink.com/account) page, click "Your Subscription." On the next page, in the *Service Plan* box, click "Manage." Then, "Cancel Service." If your service is already paused, you will not see this option and you should continue to `1b`.

    B. Down to the right in the *Devices* section, there will be a button that says "Transfer." Click that. It will ask which email address to send your service to. **If you only have one dish to transfer, this can be the same email address you're already using for your existing "account."**
      
    Note: If this is your second dish your are transferring, you will get an error that the email addres you've used is already associated with a Starlink account. In this case, you will need to supply a different email address than you are already using on your first dish, unfortunately.

2. Activate your service
    
    A. Check your email. You will receive a link to activate the "new" Starlink. Clicking the "ACTIVATE STARLINK" button in the email opens a page with a window that will be pre-poulated with your dish's serial number. You will always select "NEW ACCOUNT" here.

    Note: The user flow for "EXISTING ACCOUNT" is currently broken and will attempt to ship a new dish to the checkout address you type, even though you already have a working dish.

    B. You will need to type in an arbitrary address (this one is not binding to the account; it's just to get past this step) in the region you are targeting. If Starlink finds this address, it will allow you to click a plan and continue. **I recommend Roam**. You will add this to your cart and check out.

    C. Finally, you will check out, choosing the country you wish to activate your dish with (in my case, New Zealand), then entering some real arbitrary address that you do not require any affiliation with; it just has to be a real place. During the checkout process, it asks for card information. I have a US-based credit card. Although the payment process does not ask for a country in the payment fields, I was able to pay with my card for both dishes, no problem.

3. Profit

    A. You may notice that your "account" page has a new drop-down, if you were to click your username icon in the top-right of the window. This is related to what I mentioned earlier, that a Starlink "account" is just a combination of your email address and some address/country. With the same login credentials, you now have these two "accounts" (one per country). One account (the original) will no longer have a device associated with it and one (the new one) will have the existing dish associated with it.

    B. If your device says "Restricted if you were to open the mobile app after connecting," don't worry, this is expected. Your service will resume within the next fifteen minutes.

    C. Take note of the fact that depending on which region you are coming from and which one you are switching to, you may be saving some money. In my case, switching from a US to New Zealand account saves me over $100 USD per month. I no longer have the 50 GBs of "Mobile Priority" data at the top of each billing cycle, but that is not important, consdiering the lack of bandwidth saturation in these remote region that I am (and perhaps you are) in.

## TLDR

1. Transfer your dish to yourself in a more favorable region
2. Switch to the "Roam Unlimited" plan

