from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from core.choice import USAC_ENTITY_TYPE, USAC_ENTITY_STATUS, \
    USAC_498_STATUS, USAC_URBAN_RURAL, YESNO


class Enitity(models.Model):
    row_id = models.CharField(
        verbose_name='Entity Row ID',
        help_text='The Row ID from the USAC OData service for this BEN.',
        max_length=255,
        unique=True,
        required=True,
        blank=False,
    )
    entity_name = models.CharField(
        verbose_name='Entity Name',
        help_text='Name of entity.',
        max_length=255,
        unique=False,
        required=True,
        blank=False,
    )
    entity_number = models.CharField(
        verbose_name='Billed Entity Number',
        help_text='The number of the entity assigned by USAC.',
        max_length=8,
        unique=True,
        required=True,
        blank=False,
    )
    entity_type = models.CharField(
        verbose_name='Entity Type',
        help_text=(
            'The type of the entity including school district, school, '
            'library system, library, consortium, and '
            'non-instructional facility (NIF).'
        ),
        max_length=32,
        choices=USAC_ENTITY_TYPE,
        unique=False,
        required=True,
        blank=False,
    )
    parent = models.ManyToManyField(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Parent Entities',
        help_text=(
            'This field is blank if the entity does not have a parent.'
        ),
        symmetrical=False,
        blank=True,
        required=False,
        unique=False,
        related_name='parents',
    )
    child = models.ManyToManyField(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Child Entities',
        help_text=(
            'This field is blank if the entity does not have a child.'
        ),
        symmetrical=False,
        blank=True,
        required=False,
        unique=False,
        related_name='children',
    )
    fcc_registration_number = models.CharField(
        verbose_name='FCC Registration Number',
        help_text=(
            'The FCC Registration Number (FRN) associated with this '
            'entity, if one exists.'
        ),
        max_length=10,
        unique=True,
        null=False,
        blank=False,
    )
    status = models.BooleanField(
        verbose_name='Entity Status',
        help_text=(
            'Indicates if an organization is active (open) [True] or '
            'closed [False].'
        ),
        choices=USAC_ENTITY_STATUS,
        default=True,
        unique=False,
        null=False,
        blank=False,
    )
    fcc_form_498_form_number = models.CharField(
        verbose_name='FCC Form 498 Form Number',
        help_text=(
            'Unique (if present) number assigned to the form by USAC '
            'for an Applicant FCC Form 498.'
        ),
        max_length=20,
        unique=True,
        null=True,
        blank=True,
    )
    fcc_form_498_status_date_time = models.DateTimeField(
        verbose_name='FCC Form 498 Status Date Time',
        help_text=(
            'Date and time the last status was updated for the FCC '
            'Form 498 for the applicant.',
        ),
        unique=False,
        null=True,
        blank=True,
    )
    form498_status = models.CharField(
        verbose_name='FCC Form 498 Status',
        help_text=(
            'The status of the FCC Form 498 submitted for the entity. '
            'Every service provider is required to have a 498 ID in '
            'order to participate in any universal service program '
            'and/or receive payments from USAC.'
        ),
        max_length=15,
        choices=USAC_498_STATUS,
        unique=False,
        null=True,
        blank=True,
    )
    physical_address = models.CharField(
        verbose_name='Physical Address 1',
        help_text='Street address where the entity is located.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    physical_address_2 = models.CharField(
        verbose_name='Physical Address 2',
        help_text='Additional address information if applicable.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    physical_city = models.CharField(
        verbose_name='Physical City',
        help_text='City where the entity is located.',
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    physical_county = models.CharField(
        verbose_name='Physical County',
        help_text='County where the entity is located.',
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    physical_state = models.CharField(
        verbose_name='Physical State',
        help_text='U.S. state or territory where the entity is located.',
        max_length=2,
        unique=False,
        null=True,
        blank=True,
    )
    physical_zipcode = models.CharField(
        verbose_name='Physical Zip Code',
        help_text='Zip code for the entity.',
        max_length=10,
        unique=False,
        null=True,
        blank=True,
    )
    physical_zipcode_ext = models.CharField(
        verbose_name='Physical Zip Code Ext',
        help_text='Four-digit ZIP code extension if applicable.',
        max_length=4,
        unique=False,
        null=True,
        blank=True,
    )
    mailing_address = models.CharField(
        verbose_name='Mailing Address 1',
        help_text='Mailing address of the entity.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    mailing_address_2 = models.CharField(
        verbose_name='Mailing Address 2',
        help_text='Additional address information if applicable.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    mailing_city = models.CharField(
        verbose_name='Mailing City',
        help_text='City of the entity’s mailing address.',
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    mailing_county = models.CharField(
        verbose_name='Mailing County',
        help_text='County of the entity’s mailing address.',
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    mailing_state = models.CharField(
        verbose_name='Mailing State',
        help_text='State of the entity’s mailing address.',
        max_length=2,
        unique=False,
        null=True,
        blank=True,
    )
    mailing_zipcode = models.CharField(
        verbose_name='Mailing Zip Code',
        help_text='ZIP code of the entity’s mailing address.',
        max_length=10,
        unique=False,
        null=True,
        blank=True,
    )
    mailing_zipcode_ext = models.CharField(
        verbose_name='Mailing Zip Code Ext',
        help_text='Four-digit ZIP code extension if applicable.',
        max_length=4,
        unique=False,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name='Phone Number',
        help_text='Entity’s phone number.',
        max_length=15,
        unique=False,
        null=True,
        blank=True,
    )
    email_address = models.EmailField(
        verbose_name='Email',
        help_text='Email address for the entity’s EPC profile.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    website_url = models.URLField(
        verbose_name='Website URL',
        help_text='Entity’s website.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    account_administrator_name = models.CharField(
        verbose_name='Account Administrator Name',
        help_text='Name of the account administrator in EPC.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    general_contact_name = models.CharField(
        verbose_name='General Contact Name',
        help_text='General contact of the entity.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    general_contact_email = models.EmailField(
        verbose_name='General Contact Email',
        help_text='Email address for the general contact.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    latitude = models.DecimalField(
        verbose_name='Latitude',
        help_text=(
            'System-generated latitude coordinate of the entity based '
            'on the physical address.'
        ),
        max_digits=10,
        decimal_places=7,
        unique=False,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        verbose_name='Longitude',
        help_text=(
            'System-generated longitude coordinate of the entity based '
            'on the physical address.'
        ),
        max_digits=10,
        decimal_places=7,
        unique=False,
        null=True,
        blank=True,
    )
    user_entered_urban_rural_status = models.CharField(
        verbose_name='User-Entered Urban/Rural Status',
        help_text='User-entered urban/rural status for the entity.',
        max_length=5,
        choices=USAC_URBAN_RURAL,
        unique=False,
        null=True,
        blank=True,
        )
    urban_rural_status = models.CharField(
        verbose_name='Urban/Rural Status',
        help_text=(
            'System-generated urban/rural status for the entity based '
            'on the physical address, latitude, and longitude.'
        ),
        max_length=5,
        choices=USAC_URBAN_RURAL,
        unique=False,
        null=True,
        blank=True,
    )
    category_one_discount_rate = models.DecimalField(
        verbose_name='Category One Discount Rate',
        help_text=(
            'Discount rate for Category One services, per the entity’s '
            'EPC profile. Services discounted by this rate include '
            'Internet Access Services and/or Data Transmission but do '
            'not include Voice Services. Only applicable to '
            'non-consortium independent entities.'
        ),
        max_digits=3,
        decimal_places=2,
        unique=False,
        null=True,
        blank=True,
    )
    category_two_discount_rate = models.DecimalField(
        verbose_name='Category Two Discount Rate',
        help_text=(
            'Discount rate for Category Two services, per the entity’s '
            'EPC profile. Services discounted by this rate include '
            'Internal Connections, Managed Internal Broadband Services '
            '(MIBS) and/or Basic Maintenance of Internal Connections. '
            'Only applicable to non-consortium independent entities.'
        ),
        max_digits=3,
        decimal_places=2,
        unique=False,
        null=True,
        blank=True,
    )
    is_school_library_independent = models.BooleanField(
        verbose_name='Is School/Library Independent',
        help_text=(
            'A school/library is listed as independent (Yes) if their '
            'EPC entity profile indicates the school/library is not '
            'part of a school district/library system. All school '
            'districts, library systems, and consortia are listed as '
            'independent (Yes).'
        ),
        choices=YESNO,
        default=True,
        unique=False,
        null=True,
        blank=True,
    )
    private_school_district = models.BooleanField(
        verbose_name='Private School District',
        help_text=(
            'Indicates if school district is a private school district.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    public_school_district = models.BooleanField(
        verbose_name='Public School District',
        help_text=(
            'Indicates if school district is a public school district.'
        ),
        choices=YESNO,
        default=True,
        unique=False,
        null=True,
        blank=True,
    )
    esa_school_district = models.BooleanField(
        verbose_name='Educational Service Agency (ESA) School District',
        help_text=(
            'Indicates if a school district identifies as having an '
            'ESA support its member schools.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    charter_school_district = models.BooleanField(
        verbose_name='Charter School District',
        help_text=(
            'Indicates if a school district consists exclusively of '
            'charter schools.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    c2_student_count_reporting_type = models.CharField(
        verbose_name='C2 Student Count Reporting Type',
        help_text=(
            'Indicates how the school district reports the student '
            'count for its C2 budget calculation.'
        ),
        max_length=50,
        unique=False,
        null=True,
        blank=True,
    )
    c2_district_student_count = models.IntegerField(
        verbose_name='C2 District Student Count',
        help_text=(
            'Number of full time students for a school district’s C2 '
            'Budget calculation based on the entity profile or an '
            'approved FCC Form 471.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    c2_school_student_count = models.IntegerField(
        verbose_name='C2 School Student Count',
        help_text=(
            'Number of full time students for independent or dependent '
            'schools’ C2 budget calculations based on the entity '
            'profile or an approved FCC Form 471.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    main_library_branch_school_district = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Main Library Branch School District',
        help_text=(
            'Indicates the school district in which the main library '
            'branch is located'
        ),
        symmetrical=False,
        blank=True,
        required=False,
        unique=False,
        related_name='library_branch_school_district',
    )
    private_library_system = models.BooleanField(
        verbose_name='Private Library System',
        help_text=(
            'Indicates if the library system consists exclusively of '
            'private libraries.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    public_library_system = models.BooleanField(
        verbose_name='Public Library System',
        help_text=(
            'Indicates if the library system consists exclusively of '
            'public libraries.'
        ),
        choices=YESNO,
        default=True,
        unique=False,
        null=True,
        blank=True,
    )
    esa_consortium = models.BooleanField(
        verbose_name='Educational Service Agency (ESA) Consortium',
        help_text=(
            'An established ESA serving as a consortium leader, '
            'aggregating demand and assisting in bulk purchases on '
            'behalf of some or all of the school districts and/or '
            'libraries in its service area.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    non_profit_purchasing_group = models.BooleanField(
        verbose_name='Non-Profit Purchasing Group',
        help_text=(
            'Indicates if the consortium is part of a non-profit '
            'purchasing group.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    state_wide = models.BooleanField(
        verbose_name='State-Wide Consortium',
        help_text=(
            'Indicates if the consortium is a state-wide consortium'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    state_education_agency = models.BooleanField(
        verbose_name='State Education Agency',
        help_text=(
            'Indicates if the consortium is a state education agency.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    state_library_agency_consortium = models.BooleanField(
        verbose_name='State Library Agency - Consortium',
        help_text=(
            'Indicates if the consortium is a state library agency.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    other_state_agency = models.BooleanField(
        verbose_name='Other State Agency',
        help_text=(
            'Indicates if the consortium is a state agency other than '
            'the state agencies listed above.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    fscs_key = models.CharField(
        verbose_name='Federal-State Cooperative System',
        help_text='Indicates the FSCS of the library.',
        max_length=8,
        unique=True,
        null=True,
        blank=True,
    )
    fscs_seq = models.CharField(
        verbose_name='Federal-State Cooperative System Code (FSCS) Key',
        help_text=(
            'Library FSCS sequence code is a unique 3-digit suffix '
            'that distinguishes outlets associated with a library '
            'system'
        ),
        max_length=3,
        unique=True,
        null=True,
        blank=True,
    )
    locale_code = models.CharField(
        verbose_name='Locale Code',
        help_text=(
            'Code assigned by the Institute for Museum and Library '
            'Services (IMLS) that identifies the population density of '
            'the library’s location. Libraries that are located in the '
            'IMLS locale code of 11-City, Large; 12-City, Midsize; or '
            '21-Suburb are eligible for a higher pre-discount budget '
            'than libraries with other locale codes.'
        ),
        max_length=8,
        unique=True,
        null=True,
        blank=True,
    )
    square_footage = models.IntegerField(
        verbose_name='Square Footage',
        help_text=(
            'Total interior area of the library measured in square '
            'footage.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    academic = models.BooleanField(
        verbose_name='Academic Library',
        help_text=(
            'Indicates if the library is part of an educational '
            'institution.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    bookmobile = models.BooleanField(
        verbose_name='Bookmobile',
        help_text='Indicates if the library is a mobile library.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    kiosk = models.BooleanField(
        verbose_name='Kiosk',
        help_text='Indicates if the library is a kiosk.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    main_branch = models.BooleanField(
        verbose_name='Main Branch',
        help_text=(
            'Indicates if the library is the main branch of the '
            'library system in which it is located. Main branch will '
            'also be listed as “Yes” for independent libraries.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    new_construction_library = models.BooleanField(
        verbose_name='New Construction Library',
        help_text=(
            'Indicates if the library has not been fully constructed.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    private_library = models.BooleanField(
        verbose_name='Private Library',
        help_text='Indicates if the library is private.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    public_library = models.BooleanField(
        verbose_name='Public Library',
        help_text='Indicates if the library is public.',
        choices=YESNO,
        default=True,
        unique=False,
        null=True,
        blank=True,
    )
    research_library = models.BooleanField(
        verbose_name='Research Library',
        help_text='Indicates if the library is a research library.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    state_library_agency_library = models.BooleanField(
        verbose_name='State Library Agency - Library',
        help_text=(
            'Indicates if the library is part of a state library '
            'agency.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    tribal_library = models.BooleanField(
        verbose_name='Tribal Library',
        help_text=(
            'An E-Rate applicant may self-identify as a Tribal entity '
            'in their EPC entity profile if the majority of library '
            'patrons served are Tribal members; the entity is located '
            'partially or entirely on Tribal land; or the entity is a '
            'library operated by a Tribal Nation.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    state_school_code = models.CharField(
        verbose_name='State School Code',
        help_text='Code assigned by the state for a school.',
        max_length=32,
        unique=True,
        null=True,
        blank=True,
    )
    state_lea_code = models.CharField(
        verbose_name='State Local Education Agency (LEA) Code',
        help_text='LEA code for the school district.',
        max_length=32,
        unique=True,
        null=True,
        blank=True,
    )
    nces_public_state_code = models.CharField(
        verbose_name='NCES Public State Code',
        help_text=(
            'Code assigned by the National Center for Education '
            'Statistics (NCES) for the state.'
        ),
        max_length=2,
        unique=False,
        null=True,
        blank=True,
    )
    nces_public_district_code = models.CharField(
        verbose_name='NCES Public District Code',
        help_text='Code assigned by NCES for the school district.',
        max_length=8,
        unique=False,
        null=True,
        blank=True,
    )
    nces_public_building_code = models.CharField(
        verbose_name='NCES Public Building Code',
        help_text=(
            'Code assigned by NCES for the public school building.'
        ),
        max_length=8,
        unique=False,
        null=True,
        blank=True,
    )
    nces_private_school_id = models.CharField(
        verbose_name='NCES Private School ID',
        help_text='ID assigned by NCES for the private school.',
        max_length=8,
        unique=False,
        null=True,
        blank=True,
    )
    number_of_full_time_students = models.IntegerField(
        verbose_name='Total Number of Full-Time Students',
        help_text=(
            'The total number of full-time students for the school.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    total_number_of_part_time_students = models.IntegerField(
        verbose_name='Total Number of Part-Time Students',
        help_text=(
            'The total number of part-time students for the school.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    peak_number_of_part_time_students = models.IntegerField(
        verbose_name='Peak Number of Part-Time Students',
        help_text=(
            'The peak number of part-time students for the school.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    number_of_nslp_students = models.IntegerField(
        verbose_name='Number of NSLP Students',
        help_text=(
            'Number of students or calculated number of students '
            'eligible for the National School Lunch Program (NSLP).'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    community_eligibility_program_cep = models.BooleanField(
        verbose_name='Community Eligibility Program (CEP)',
        help_text=(
            'Indicates if the school is enrolled in the Community '
            'Eligibility Program (CEP).'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    cep_percentage = models.DecimalField(
        verbose_name='CEP Percentage',
        help_text=(
            'Indicates the approved percentage of a school in the '
            'Community Eligibility Program (CEP).'
        ),
        max_digits=3,
        decimal_places=2,
        unique=False,
        null=True,
        blank=True,
    )
    alternative_discount_method = models.BooleanField(
        verbose_name='Alternative Discount Method',
        help_text=(
            'Indicates the school’s alternative discount method such '
            'as sibling match, survey, or combination (not CEP).'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    does_this_organization_have_an_endowment = models.BooleanField(
        verbose_name='Does This Organization Have an Endowment',
        help_text='Indicates whether the organization has an endowment.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    bie = models.BooleanField(
        verbose_name='Bureau of Indian Education (BIE)',
        help_text=(
            'A school operated by the Bureau of Indian Education (BIE).'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    charter_school = models.BooleanField(
        verbose_name='Charter School',
        help_text='A charter school.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    dormitory = models.BooleanField(
        verbose_name='Dormitory',
        help_text='A dormitory for housing students.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    esa_school = models.BooleanField(
        verbose_name='ESA School',
        help_text=(
            'A school operated by an Educational Service Agency to '
            'provide specialized services such as Vocational or '
            'Special Education..'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    esa_school_district_with_no_schools = models.BooleanField(
        verbose_name='ESA School District with No Schools',
        help_text=(
            'An Educational State Agency (ESA) comprised entirely of '
            'non-instructional facilities (NIFs), from which its staff '
            'is based. It may run education programs in facilities '
            'that are not recognized as elementary or secondary '
            'schools. Classifying such an entity as a school in EPC is '
            'necessary to be able to enter the total student count for '
            'all of its member school districts.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    head_start = models.BooleanField(
        verbose_name='Head Start',
        help_text=(
            'A facility with a comprehensive child development program '
            'that serves preschool-age children and their families.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    juvenile_justice = models.BooleanField(
        verbose_name='Juvenile Justice',
        help_text=(
            'A NIF which is (and should be) labeled as a school in '
            'EPC, but usually has within it a primary or secondary '
            'education program.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    new_construction_school = models.BooleanField(
        verbose_name='New Construction School',
        help_text=(
            'A school that has yet to be fully constructed, often '
            'requiring estimated student counts.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    pre_k = models.BooleanField(
        verbose_name='Pre-K',
        help_text='A Pre-K school.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    private_school = models.BooleanField(
        verbose_name='Private School',
        help_text='A private school.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    public_school = models.BooleanField(
        verbose_name='Public School',
        help_text='A public school.',
        choices=YESNO,
        default=True,
        unique=False,
        null=True,
        blank=True,
    )
    tribal_school = models.BooleanField(
        verbose_name='Tribal School',
        help_text=(
            'An E-Rate applicant may self-identify as a Tribal entity '
            'in their EPC entity profile if the majority of students '
            'served are Tribal members; the entity is located '
            'partially or entirely on Tribal land; the entity is a '
            'school operated by or receiving funding from the Bureau '
            'of Indian Education (BIE); or the entity is a school by a '
            'Tribal Nation.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    adult_education = models.BooleanField(
        verbose_name='Adult Education',
        help_text='An institution for adult education.',
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    swing_space = models.BooleanField(
        verbose_name='Swing Space',
        help_text=(
            'An institution that temporarily houses students from a '
            'school which is considered the "main entity" or original '
            'location of the student population.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    detention_center = models.BooleanField(
        verbose_name='Detention Center',
        help_text=(
            'A facility that is treated in the same way as a juvenile '
            'justice facility.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    general_use_school = models.BooleanField(
        verbose_name='General Use School',
        help_text=(
            'A school that offers instruction to students drawn from '
            'other schools, and student counts can change throughout '
            'the year.'
        ),
        choices=YESNO,
        default=False,
        unique=False,
        null=True,
        blank=True,
    )
    tribal_affiliation = models.CharField(
        verbose_name='Tribal Affiliation',
        help_text=(
            'Selected name of the federally recognized Tribal Nation '
            'that the entity is affiliated with from the entity’s EPC '
            'profile listed drop down options.'
        ),
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    other_tribe_name = models.CharField(
        verbose_name='Other Tribe Name',
        help_text=(
            'Typed name of the federally recognized Tribal Nation that '
            'the entity is affiliated with when "Other" is selected '
            'for Tribal Affiliation.'
        ),
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    entity_last_modified_by = models.EmailField(
        verbose_name='Entity Last Modified By',
        help_text=(
            'Indicates the e-mail address of the person who last '
            'modified the entity’s information in EPC.'
        ),
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    last_updated_date_time = models.DateTimeField(
        verbose_name='Last Updated Date Time',
        help_text=(
            'Indicates the date and time the profile of the entity was '
            'last modified in EPC.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name='Created',
        help_text='The date and time this record was created in Djano.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        help_text='The date and time this record was last updated in Django.',
        auto_now=True,
    )
    
    class Meta:
        ordering = ('entity_number',)
        verbose_name = 'Billed Entity Information'
        verbose_name_plural = 'Billed Entities Information'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__ (self):
        return str(f'{self.entity_number}')
    
    def get_absolute_url(self):
        return reverse('core:ben', kwargs={'pk': self.pk})


class Annex(models.Model):
    entity = models.ForeignKey(
        Enitity,
        on_delete=models.CASCADE,
        verbose_name='Annex Parent Organization',
        help_text='Entity the annex is connected to',
        related_name='annexes',
        null=False,
        blank=False,
    )
    annex_name = models.CharField(
        verbose_name='Annex Name',
        help_text='Name of the annex.',
        max_length=255,
        unique=False,
        null=False,
        blank=False,
    )
    annex_organization_id = models.IntegerField(
        verbose_name='Annex Organization ID',
        help_text='Unique identifier for each annex.',
        unique=True,
        null=False,
        blank=False,
    )
    annex_address = models.CharField(
        verbose_name='Annex Address',
        help_text='The physical address of the annex.',
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    annex_city = models.CharField(
        verbose_name='Annex City',
        help_text='City where the annex is located.',
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    annex_county = models.CharField(
        verbose_name='Annex County',
        help_text='County where the annex is located.',
        max_length=100,
        unique=False,
        null=True,
        blank=True,
    )
    annex_state = models.CharField(
        verbose_name='Annex State',
        help_text='U.S. state or territory where the annex is located.',
        max_length=2,
        unique=False,
        null=True,
        blank=True,
    )
    annex_zipcode = models.CharField(
        verbose_name='Annex Zip Code',
        help_text='ZIP code where the annex is located.',
        max_length=10,
        unique=False,
        null=True,
        blank=True,
    )
    annex_phone = models.CharField(
        verbose_name='Annex Phone',
        help_text='Phone number to reach the annex.',
        max_length=15,
        unique=False,
        null=True,
        blank=True,
    )
    annex_last_modified_by = models.EmailField(
        verbose_name='Annex Last Modified By',
        help_text=(
            'E-mail address of the person who last modified the '
            'annex’s information in EPC.'
        ),
        max_length=255,
        unique=False,
        null=True,
        blank=True,
    )
    last_updated_date_time = models.DateTimeField(
        verbose_name='Last Updated',
        help_text=(
            'Indicates the date and time a user last updated annex '
            'data in EPC.'
        ),
        unique=False,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name='Created',
        help_text='The date and time this record was created in Djano.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        help_text='The date and time this record was last updated in Django.',
        auto_now=True,
    )
    
    class Meta:
        ordering = ('annex_organization_id',)
        verbose_name = 'Annex Information'
        verbose_name_plural = 'Annexes Information'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__ (self):
        return str(f'{self.annex_organization_id}')
    
    def get_absolute_url(self):
        return reverse('core:annex', kwargs={'pk': self.pk})


class UserEntity(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='User',
        help_text='User linked to these entities.',
        on_delete=models.CASCADE
    )
    entity = models.ManyToManyField(
        Enitity,
        on_delete=models.CASCADE,
        verbose_name='Entities',
        help_text='Entities linked to this user.',
        related_name='users',
        blank=True,
    )

    def __str__(self):
        return f'{self.user} - {str(self.ben)}'
    

    class Meta:
        ordering = ('user',)
        verbose_name = 'User to Entity'
        verbose_name_plural = 'User to Entities'
