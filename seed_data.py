"""
Seed data script for EveShield application.
Run this script after migrations to populate initial data.

Usage: python manage.py shell < seed_data.py
Or: python manage.py shell, then copy-paste this content
"""

from django.utils.text import slugify

from EveShieldApp import models

# Clear existing data (optional - comment out if you want to keep existing data)
# models.Lawyer.objects.all().delete()
# models.Therapist.objects.all().delete()
# models.ResourceArticle.objects.all().delete()

# Seed Lawyers
lawyers_data = [
    {
        'name': 'Advocate Sarah Wanjiku',
        'phone': '+254712345678',
        'whatsapp': '+254712345678',
        'email': 'sarah.wanjiku@lawfirm.co.ke',
        'county': 'Nairobi',
        'specialization': 'GBV cases, Family Law, Criminal Law',
        'address': 'Upper Hill, Nairobi',
    },
    {
        'name': 'Legal Aid Center - Mombasa',
        'phone': '+254723456789',
        'whatsapp': '+254723456789',
        'email': 'info@legalaidmombasa.co.ke',
        'county': 'Mombasa',
        'specialization': 'GBV cases, Pro bono services, Legal representation',
        'address': 'Mombasa CBD',
    },
    {
        'name': 'Advocate James Ochieng',
        'phone': '+254734567890',
        'whatsapp': '+254734567890',
        'email': 'james.ochieng@law.co.ke',
        'county': 'Kisumu',
        'specialization': 'GBV cases, Human Rights, Constitutional Law',
        'address': 'Kisumu Town',
    },
    {
        'name': 'FIDA Kenya - Nairobi Branch',
        'phone': '+254745678901',
        'whatsapp': '+254745678901',
        'email': 'nairobi@fida-kenya.org',
        'county': 'Nairobi',
        'specialization': 'Women\'s rights, GBV cases, Legal aid for women',
        'address': 'Westlands, Nairobi',
    },
    {
        'name': 'Advocate Mary Akinyi',
        'phone': '+254756789012',
        'whatsapp': '+254756789012',
        'email': 'mary.akinyi@lawfirm.co.ke',
        'county': 'Nakuru',
        'specialization': 'GBV cases, Family Law, Protection Orders',
        'address': 'Nakuru Town',
    },
    {
        'name': 'Legal Services Center - Eldoret',
        'phone': '+254767890123',
        'whatsapp': '+254767890123',
        'email': 'info@legalserviceseldoret.co.ke',
        'county': 'Uasin Gishu',
        'specialization': 'GBV cases, Legal representation, Court processes',
        'address': 'Eldoret Town',
    },
]

for lawyer_data in lawyers_data:
    models.Lawyer.objects.get_or_create(
        name=lawyer_data['name'],
        defaults=lawyer_data
    )
    print(f"Created/Updated lawyer: {lawyer_data['name']}")

# Seed Therapists
therapists_data = [
    {
        'name': 'Dr. Grace Muthoni',
        'specialty': 'Trauma counseling, PTSD, Domestic violence support',
        'phone': '+254712345679',
        'email': 'grace.muthoni@therapy.co.ke',
        'county': 'Nairobi',
        'address': 'Westlands, Nairobi',
        'qualifications': 'PhD in Clinical Psychology',
    },
    {
        'name': 'Counselor Amina Hassan',
        'specialty': 'Trauma counseling, Anxiety, Depression',
        'phone': '+254723456790',
        'email': 'amina.hassan@counseling.co.ke',
        'county': 'Mombasa',
        'address': 'Mombasa CBD',
        'qualifications': 'MSc in Counseling Psychology',
    },
    {
        'name': 'Dr. Peter Otieno',
        'specialty': 'Trauma counseling, GBV survivor support, Mental health',
        'phone': '+254734567891',
        'email': 'peter.otieno@therapy.co.ke',
        'county': 'Kisumu',
        'address': 'Kisumu Town',
        'qualifications': 'PhD in Psychology',
    },
    {
        'name': 'Counselor Jane Wanjiru',
        'specialty': 'Trauma counseling, Stress management, Self-care',
        'phone': '+254745678902',
        'email': 'jane.wanjiru@counseling.co.ke',
        'county': 'Nairobi',
        'address': 'Karen, Nairobi',
        'qualifications': 'MSc in Clinical Psychology',
    },
    {
        'name': 'Dr. Susan Kamau',
        'specialty': 'Trauma counseling, PTSD, Anxiety disorders',
        'phone': '+254756789013',
        'email': 'susan.kamau@therapy.co.ke',
        'county': 'Nakuru',
        'address': 'Nakuru Town',
        'qualifications': 'PhD in Clinical Psychology',
    },
    {
        'name': 'Counselor David Kipchoge',
        'specialty': 'Trauma counseling, Mental health support, Crisis intervention',
        'phone': '+254767890124',
        'email': 'david.kipchoge@counseling.co.ke',
        'county': 'Uasin Gishu',
        'address': 'Eldoret Town',
        'qualifications': 'MSc in Counseling Psychology',
    },
]

for therapist_data in therapists_data:
    models.Therapist.objects.get_or_create(
        name=therapist_data['name'],
        defaults=therapist_data
    )
    print(f"Created/Updated therapist: {therapist_data['name']}")

# Seed Resource Articles
articles_data = [
    {
        'title': 'Know Your Rights as a GBV Survivor',
        'slug': 'know-your-rights',
        'content': '''As a survivor of gender-based violence, you have fundamental rights that are protected by law:

1. **Right to Report**: You have the right to report any incident of GBV to the police. The police are legally obligated to take your report seriously and investigate.

2. **Right to Medical Care**: You have the right to receive medical attention, including a medical examination and treatment for any injuries.

3. **Right to Legal Representation**: You have the right to legal counsel. You can access free legal aid services or hire a private lawyer.

4. **Right to Protection**: You have the right to protection from further harm. You can apply for a protection order from the court.

5. **Right to Privacy**: Your personal information and the details of your case should be kept confidential.

6. **Right to Support Services**: You have the right to access counseling, shelter (if needed), and other support services.

7. **Right to Fair Treatment**: You should be treated with dignity and respect, without discrimination based on gender, age, or any other factor.

Remember: No one has the right to harm you. The law is on your side.''',
        'category': 'rights',
    },
    {
        'title': 'How to File a GBV Complaint',
        'slug': 'how-to-file-complaint',
        'content': '''Filing a complaint about gender-based violence is an important step toward seeking justice. Here's how to do it:

**Step 1: Report to Police**
- Go to the nearest police station
- Request to file a report
- Provide as much detail as possible about the incident
- Request a P3 form for medical examination

**Step 2: Medical Examination**
- Take the P3 form to a government hospital or approved medical facility
- A qualified medical officer will examine you and fill out the form
- This form is crucial evidence in court

**Step 3: Legal Support**
- Contact a lawyer from our Legal Aid Directory
- They can guide you through the legal process
- Many lawyers offer pro bono services for GBV cases

**Step 4: Protection Order (if needed)**
- Apply for a protection order at the nearest court
- This can prevent the abuser from contacting you
- Violation of a protection order is a criminal offense

**Step 5: Follow Up**
- Keep copies of all documents
- Follow up with the police on your case
- Stay in touch with your lawyer

Remember: You don't have to go through this alone. Support is available.''',
        'category': 'complaint',
    },
    {
        'title': 'Emergency Steps: What to Do Immediately',
        'slug': 'emergency-steps',
        'content': '''If you're experiencing gender-based violence or are in immediate danger, here's what to do:

**If You're in Immediate Danger:**
1. **Call 999** - Police emergency services
2. **Call 1195** - National GBV Hotline
3. Get to a safe place if possible
4. Contact someone you trust

**After Ensuring Your Safety:**
1. **Seek Medical Attention**: Go to the nearest hospital if you have injuries
2. **Document Everything**: Take photos of injuries, save messages, keep records
3. **Report to Police**: File a report at the nearest police station
4. **Get Legal Help**: Contact a lawyer from our directory
5. **Access Support**: Reach out to counselors or therapists

**Important Documents to Collect:**
- Medical reports (P3 form)
- Police report
- Photos of injuries
- Text messages, emails, or other evidence
- Witness statements (if any)

**Safety Planning:**
- Identify safe places you can go
- Keep emergency contacts handy
- Have important documents ready
- Consider applying for a protection order

**Remember:**
- Your safety is the top priority
- You are not to blame
- Help is available
- You don't have to face this alone''',
        'category': 'emergency',
    },
    {
        'title': 'Understanding Protection Orders',
        'slug': 'protection-orders',
        'content': '''A Protection Order is a court order that protects you from an abuser. Here's what you need to know:

**What is a Protection Order?**
A Protection Order is a legal document issued by a court that prohibits an abuser from:
- Contacting you
- Coming near you or your home
- Harassing or threatening you
- Entering your workplace or children's school

**How to Apply:**
1. Go to the nearest Magistrate's Court
2. Fill out an application form (you can do this yourself or through a lawyer)
3. The court can issue temporary orders immediately if you're in danger
4. The abuser will be served with the order
5. A hearing will be scheduled

**What Happens Next:**
- The court will hold a hearing
- Both parties can present their case
- The court will decide whether to grant a permanent order
- The order is valid for a specified period (usually 1-2 years)

**If the Order is Violated:**
- Violation of a protection order is a criminal offense
- Report violations to the police immediately
- The abuser can be arrested and charged

**Important Notes:**
- Protection orders are free to apply for
- You don't need a lawyer, but it's recommended
- Keep a copy of the order with you at all times
- Give copies to trusted family members or friends

**Getting Help:**
- Contact a lawyer from our Legal Aid Directory
- They can help you with the application process
- Many organizations provide free assistance with protection orders''',
        'category': 'rights',
    },
    {
        'title': 'Self-Care for GBV Survivors',
        'slug': 'self-care-survivors',
        'content': '''Taking care of yourself is crucial when dealing with the aftermath of gender-based violence. Here are important self-care strategies:

**Physical Self-Care:**
- Get enough sleep (7-9 hours per night)
- Eat regular, nutritious meals
- Stay hydrated
- Exercise regularly (even light walking helps)
- Attend medical appointments

**Emotional Self-Care:**
- Allow yourself to feel your emotions
- Practice self-compassion - be kind to yourself
- Journal your thoughts and feelings
- Engage in activities you enjoy
- Set boundaries with others

**Mental Self-Care:**
- Practice grounding exercises when feeling overwhelmed
- Try deep breathing exercises
- Consider meditation or mindfulness
- Limit exposure to triggering content
- Take breaks when needed

**Social Self-Care:**
- Connect with supportive people
- Join support groups if available
- Don't isolate yourself
- Ask for help when you need it
- Set boundaries with toxic relationships

**Professional Support:**
- Consider therapy or counseling
- Join support groups for survivors
- Work with a trauma-informed therapist
- Access mental health services

**Important Reminders:**
- Healing takes time - be patient with yourself
- There's no "right" way to heal
- It's okay to have good days and bad days
- You're stronger than you know
- You deserve support and care

**When to Seek Professional Help:**
- If you're having thoughts of self-harm
- If symptoms are interfering with daily life
- If you're struggling to function
- If you feel overwhelmed or unsafe

Remember: Self-care is not selfish - it's necessary for your healing journey.''',
        'category': 'support',
    },
]

for article_data in articles_data:
    models.ResourceArticle.objects.get_or_create(
        slug=article_data['slug'],
        defaults=article_data
    )
    print(f"Created/Updated article: {article_data['title']}")

print("\n✅ Seed data creation completed!")
print(f"Created {len(lawyers_data)} lawyers")
print(f"Created {len(therapists_data)} therapists")
print(f"Created {len(articles_data)} resource articles")

