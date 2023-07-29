import openai
import langchain
from langchain.llms import OpenAI
from langchain import PromptTemplate
from train_ex import examples




### using open ai and langchian instance to efficiently train and interact with the llm
from langchain import LLMChain
llm = OpenAI(
    temperature=0,
    openai_api_key="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",
    model_name="gpt-3.5-turbo-16k" # can be used with llms like 'gpt-3.5-turbo'
)



## for training we are using FewShot prompt template as it suits our case best
from langchain import PromptTemplate, FewShotPromptTemplate


# Next, we specify the template to format the examples we have provided.
# We use the `PromptTemplate` class for this.
example_template = """
User: {query}
AI: {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template,
)


# Finally, we create the `FewShotPromptTemplate` object.
few_shot_prompt = FewShotPromptTemplate(
    # These are the examples we want to insert into the prompt.
    examples=examples,
    # This is how we want to format the examples when we insert them into the prompt.
    example_prompt=example_prompt,
    # The prefix is some text that goes before the examples in the prompt.
    # Usually, this consists of intructions.
    prefix = """
        You are an data entry and application writer for the Certificate of Lawful Use for Short-term Let Accommodation: Planning Statement.
        You will be given all the necessary information about the applicant in the input and your task is to follow a specific application format that will be provided and update that application text with the new information given to you as a text.
        As you are an application writer and data entry operator so there is nothing else expected from you. only respond to query that has new information in specific format and rewrite the application text in exact same pattern and patterns like numbering etc must be followed.
        Also you must not reply with any other answer.you must only asnwer with the regenerated same pattern application from the input information given to you.
        Below is the exact sample format that will always and must be followed by pattern and writing style , only you will rewrite the texts in it with the new information and in application writing style as in the text below:
        Pattern to follow and Section wise text:
        1.	Introduction
        1.1.1.	Contour Town Planning has been asked to provide a planning statement in support of this application to the City of Edinburgh Council (‘the Council’) by Iain Muirhead (‘the applicant’) for a Certificate of Lawfulness of Existing Use or Development (‘CLEUD’) in respect of the use of the subject property (the flat) in his/her ownership at (address here and info change here).
        1.1.2.	The flat has been used as short term let visitor accommodation since July 2022 (date may change). The purpose of this application is to demonstrate as described in Section 150 (2) of the Town and Country Planning (Scotland) Act 1997 (as amended), ‘The Planning Act’, that the use of the flat as short term let visitor accommodation does not constitute development as no material change of use has taken place.
        1.1.3.	For booking purposes the flat is known as the ‘Bright and Stylish Apartment in the City Centre’. (City Centre’ may change) The flat is used for short term residential letting purposes, or as a ‘self-catering holiday let’, and has been used continuously for this purpose since before the confirmation of Edinburgh’s short term let control area.
        1.1.4.	The property is indicated on the Site Location plan and Floor Plan submitted in support of this Application.
        5.	Assessment
        5.1.1.	As Lord Justice Sullivan noted in his ruling, the Planning Authority is ‘entitled’ to form a view as to whether a material change of use has taken place; based on matters of fact and degree.
        5.1.2.	Turning to the subject property at Flat 6, 77 Cumberland Street, (address change here) as already noted, the 2021 Guidance document referred to in section 4 of this Planning Statement provides a useful list of relevant matters that will allow the fact and degree of any change from a residential use to a short term let use to be assessed.
        5.1.3.	To assist the Planning Authority in its assessment of these matters, the paragraphs that follow offers some consideration of the subject property when assessed against these matters.
        The character of the new use and of the wider area
        5.1.4.	The short term let use allows visitors to the city to stay temporarily in residential properties. Very often such stays are marketed as allowing visitors to ‘live like locals’. The emphasis of such use is on visitors behaving in such a way that they feel like they are permanent residents. In this way, guests that want to give most expression to the idea of living like a local will act and behave in a manner that is practically indistinguishable from that of a permanent resident.
        5.1.5.	In terms of the character of the wider area, the property is located in Edinburgh’s New Town (town info may change). This is an explicitly urban quarter of the city, expressly laid out as such in the late 18th century and early 19th Century. In such areas, acting reasonably, both permanent residents and visitors should recognise that an urban setting like this can absorb a relatively wide range of urban activities. These might include: people coming in and out of buildings at different times of day and night; people and vehicles moving along streets at different times of day and night; and, commercial activity taking place predominantly during the day.
        5.1.6.	The property at 77 Cumberland Street (address and measurement and town info change) is located less than 50 metres from a public house with a beer garden, and less than 200 metres from an area beginning on St Stephen’s Street designated in City of Edinburgh Council’s Adopted Local Development Plan 2016 as performing a ‘town centre’ function for Stockbridge.
        5.1.7.	Overall, the immediate area surrounding the property is considered to be relatively busy where some activity is reasonably to be expected. It is considered that for many people the ongoing activity that the area supports would be regarded as a benefit rather than as an adverse outcome; and compares favourably with perhaps the vast majority of places elsewhere in Scotland where such activity does not occur. The latent activity levels that this area enjoys also means that this is an area that has shown itself capable of assimilating a range of uses together in a host urban environment that does not appear to be fragile or adversely sensitive to change.
        The size of the property
        5.1.8.	(change bedroom and max people and measurement info) The property has one double-bedroom. It is advertised as capable of hosting a maximum of 3 people. The property extends to approximately 44 sqm. This is considerably smaller than the 52sqm minimum standard for a one-bedroom residential property identified by the City of Edinburgh Council in its January 2020 Design Guidance document. The reason stated in the document for defining these minimum space standards was ‘in order to ensure satisfactory amenity’.
        5.1.9.	(change bedroom and resident count and visitor info) For the avoidance of doubt, a one-bedroom property like this would be equally capable of hosting either 3 permanent residents (a couple and a child) or 3 visitors (a couple and a child).
        The pattern of activity associated with the use including numbers of occupants, the period of use, issues of noise, disturbance and parking demand
        5.1.10.	(change guest count info) As noted above, the maximum number of guests that could stay in the property would be 3. The applicant has confirmed that a minimum stay duration of (change amount of nights and month info) 2 nights is in place throughout most of the year, with this total rising to a 4 night minimum stay in August. The applicant advises that the property is used as a short term let an average of 9 nights per calendar month.
        5.1.11.	Each guest is vetted by the hosting company that looks after its servicing. Under its own procedures, the company ensures that no-one under the age of 25 is allowed to rent the property.
        5.1.12.	All guests are required to agree to ‘house rules’ for the property at the point of booking. These rules outlaw practices such as: smoking or vaping anywhere in the property; holding parties; and keeping pets. The guest book provided with the property for each group of guests explains these rules as well as providing further detail on matters such as refuse disposal and recycling; bag storage and nearby parking; and ‘quiet periods’ in the property (between 10pm and 7.30am) (hours may change).
        5.1.13.	To assist in assessing the property against this matter, a copy of the property’s guest book as well as a copy of the hosting company’s house rules have been appended to this application as supporting documents. Overall, it is considered that there is far greater control of guest behaviour and of all activity that can take place in the property than would be the case if it was let out to a permanent resident.
        The nature and character of any services provided
        5.1.14.	For those arriving by car, guests are directed to suggested local public car parks within the guest book provided with the property. For the avoidance of doubt, the lack of car parking is made clear on the property’s online listing. Anecdotally, the hosting company has confirmed that most guests in fact arrive by train or plane and do not require parking of any description.
        5.1.15.	The property has no access to any private or shared outside amenity garden areas. (storage rules may change here) It also has no bag storage facilities on site (although again, suggested commercial outlets where bag storage is available is detailed in the guest book).
        5.1.16.	All cleaning of the property takes place after check-out/departures (10.30 am) (times listed here may change) and before check-in/arrivals (4pm). Accordingly, the servicing of the property always takes place in office hours and not during anti- social times.
        Also about the above query, the text inside the round brackets is for your understanding, you must not include this when you are re writing the application text as per above format exactly.
        must not reply with any other answer.you must only asnwer with the regenerated same pattern application from the input information given to you.
        """,
    # The suffix is some text that goes after the examples in the prompt.
    # Usually, this is where the user input will go
    suffix = """
            User: {query}
            AI: """,
    # The input variables are the variables that the overall prompt expects.
    input_variables=["query"],
    # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
    example_separator="\n\n",
)





chain = LLMChain(llm=llm, prompt=few_shot_prompt)
# Run the chain only specifying the input variable.