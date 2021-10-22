#
#  CodeSystems.py
#  client-py
#
#  Generated from FHIR 3.6.0-bd605d07 on 2018-12-20.
#  2018, SMART Health IT.
#
#  THIS HAS BEEN ADAPTED FROM Swift Enums WITHOUT EVER BEING IMPLEMENTED IN
#  Python, FOR DEMONSTRATION PURPOSES ONLY.
#


class AbstractType(object) {
	""" A list of the base types defined by this version of the FHIR specification - types that are defined, but for which only
specializations actually are created.

	URL: http://hl7.org/fhir/abstract-types
	"""
	
	type = "Type"
	""" A place holder that means any kind of data type
	"""
	
	any = "Any"
	""" A place holder that means any kind of resource
	"""
}


class AccountStatus(object) {
	""" Indicates whether the account is available to be used.

	URL: http://hl7.org/fhir/account-status
	ValueSet: http://hl7.org/fhir/ValueSet/account-status
	"""
	
	active = "active"
	""" This account is active and may be used.
	"""
	
	inactive = "inactive"
	""" This account is inactive and should not be used to track financial information.
	"""
	
	enteredInError = "entered-in-error"
	""" This instance should not have been part of this patient's medical record.
	"""
	
	onHold = "on-hold"
	""" This account is on hold.
	"""
	
	unknown = "unknown"
	""" The ccount status is unknown.
	"""
}


class ActionCardinalityBehavior(object) {
	""" Defines behavior for an action or a group for how many times that item may be repeated.

	URL: http://hl7.org/fhir/action-cardinality-behavior
	ValueSet: http://hl7.org/fhir/ValueSet/action-cardinality-behavior
	"""
	
	single = "single"
	""" The action may only be selected one time.
	"""
	
	multiple = "multiple"
	""" The action may be selected multiple times.
	"""
}


class ActionConditionKind(object) {
	""" Defines the kinds of conditions that can appear on actions.

	URL: http://hl7.org/fhir/action-condition-kind
	ValueSet: http://hl7.org/fhir/ValueSet/action-condition-kind
	"""
	
	applicability = "applicability"
	""" The condition describes whether or not a given action is applicable.
	"""
	
	start = "start"
	""" The condition is a starting condition for the action.
	"""
	
	stop = "stop"
	""" The condition is a stop, or exit condition for the action.
	"""
}


class ActionGroupingBehavior(object) {
	""" Defines organization behavior of a group.

	URL: http://hl7.org/fhir/action-grouping-behavior
	ValueSet: http://hl7.org/fhir/ValueSet/action-grouping-behavior
	"""
	
	visualGroup = "visual-group"
	""" Any group marked with this behavior should be displayed as a visual group to the end user.
	"""
	
	logicalGroup = "logical-group"
	""" A group with this behavior logically groups its sub-elements, and may be shown as a visual group to the end
	/// user, but it is not required to do so.
	"""
	
	sentenceGroup = "sentence-group"
	""" A group of related alternative actions is a sentence group if the target referenced by the action is the same in
	/// all the actions and each action simply constitutes a different variation on how to specify the details for the
	/// target. For example, two actions that could be in a SentenceGroup are "aspirin, 500 mg, 2 times per day" and
	/// "aspirin, 300 mg, 3 times per day". In both cases, aspirin is the target referenced by the action, and the two
	/// actions represent different options for how aspirin might be ordered for the patient. Note that a SentenceGroup
	/// would almost always have an associated selection behavior of "AtMostOne", unless it's a required action, in
	/// which case, it would be "ExactlyOne".
	"""
}


class ActionList(object) {
	""" List of allowable action which this resource can request.

	URL: http://hl7.org/fhir/actionlist
	ValueSet: http://hl7.org/fhir/ValueSet/actionlist
	"""
	
	cancel = "cancel"
	""" Cancel, reverse or nullify the target resource.
	"""
	
	poll = "poll"
	""" Check for previously un-read/ not-retrieved resources.
	"""
	
	reprocess = "reprocess"
	""" Re-process the target resource.
	"""
	
	status = "status"
	""" Retrieve the processing status of the target resource.
	"""
}


class ActionParticipantType(object) {
	""" The type of participant for the action.

	URL: http://hl7.org/fhir/action-participant-type
	ValueSet: http://hl7.org/fhir/ValueSet/action-participant-type
	"""
	
	patient = "patient"
	""" The participant is the patient under evaluation.
	"""
	
	practitioner = "practitioner"
	""" The participant is a practitioner involved in the patient's care.
	"""
	
	relatedPerson = "related-person"
	""" The participant is a person related to the patient.
	"""
	
	device = "device"
	""" The participant is a system or device used in the care of the patient.
	"""
}


class ActionPrecheckBehavior(object) {
	""" Defines selection frequency behavior for an action or group.

	URL: http://hl7.org/fhir/action-precheck-behavior
	ValueSet: http://hl7.org/fhir/ValueSet/action-precheck-behavior
	"""
	
	yes = "yes"
	""" An action with this behavior is one of the most frequent action that is, or should be, included by an end user,
	/// for the particular context in which the action occurs. The system displaying the action to the end user should
	/// consider "pre-checking" such an action as a convenience for the user.
	"""
	
	no = "no"
	""" An action with this behavior is one of the less frequent actions included by the end user, for the particular
	/// context in which the action occurs. The system displaying the actions to the end user would typically not "pre-
	/// check" such an action.
	"""
}


class ActionRelationshipType(object) {
	""" Defines the types of relationships between actions.

	URL: http://hl7.org/fhir/action-relationship-type
	ValueSet: http://hl7.org/fhir/ValueSet/action-relationship-type
	"""
	
	beforeStart = "before-start"
	""" The action must be performed before the start of the related action.
	"""
	
	before = "before"
	""" The action must be performed before the related action.
	"""
	
	beforeEnd = "before-end"
	""" The action must be performed before the end of the related action.
	"""
	
	concurrentWithStart = "concurrent-with-start"
	""" The action must be performed concurrent with the start of the related action.
	"""
	
	concurrent = "concurrent"
	""" The action must be performed concurrent with the related action.
	"""
	
	concurrentWithEnd = "concurrent-with-end"
	""" The action must be performed concurrent with the end of the related action.
	"""
	
	afterStart = "after-start"
	""" The action must be performed after the start of the related action.
	"""
	
	after = "after"
	""" The action must be performed after the related action.
	"""
	
	afterEnd = "after-end"
	""" The action must be performed after the end of the related action.
	"""
}


class ActionRequiredBehavior(object) {
	""" Defines expectations around whether an action or action group is required.

	URL: http://hl7.org/fhir/action-required-behavior
	ValueSet: http://hl7.org/fhir/ValueSet/action-required-behavior
	"""
	
	must = "must"
	""" An action with this behavior must be included in the actions processed by the end user; the end user SHALL NOT
	/// choose not to include this action.
	"""
	
	could = "could"
	""" An action with this behavior may be included in the set of actions processed by the end user.
	"""
	
	mustUnlessDocumented = "must-unless-documented"
	""" An action with this behavior must be included in the set of actions processed by the end user, unless the end
	/// user provides documentation as to why the action was not included.
	"""
}


class ActionSelectionBehavior(object) {
	""" Defines selection behavior of a group.

	URL: http://hl7.org/fhir/action-selection-behavior
	ValueSet: http://hl7.org/fhir/ValueSet/action-selection-behavior
	"""
	
	any = "any"
	""" Any number of the actions in the group may be chosen, from zero to all.
	"""
	
	all = "all"
	""" All the actions in the group must be selected as a single unit.
	"""
	
	allOrNone = "all-or-none"
	""" All the actions in the group are meant to be chosen as a single unit: either all must be selected by the end
	/// user, or none may be selected.
	"""
	
	exactlyOne = "exactly-one"
	""" The end user must choose one and only one of the selectable actions in the group. The user SHALL NOT choose none
	/// of the actions in the group.
	"""
	
	atMostOne = "at-most-one"
	""" The end user may choose zero or at most one of the actions in the group.
	"""
	
	oneOrMore = "one-or-more"
	""" The end user must choose a minimum of one, and as many additional as desired.
	"""
}


class ActionType(object) {
	""" The type of action to be performed.

	URL: http://terminology.hl7.org/CodeSystem/action-type
	ValueSet: http://hl7.org/fhir/ValueSet/action-type
	"""
	
	create = "create"
	""" The action is to create a new resource.
	"""
	
	update = "update"
	""" The action is to update an existing resource.
	"""
	
	remove = "remove"
	""" The action is to remove an existing resource.
	"""
	
	fireEvent = "fire-event"
	""" The action is to fire a specific event.
	"""
}


class ActivityDefinitionCategory(object) {
	""" High-level categorization of the type of activity.

	URL: http://terminology.hl7.org/CodeSystem/activity-definition-category
	ValueSet: http://hl7.org/fhir/ValueSet/activity-definition-category
	"""
	
	treatment = "treatment"
	""" The activity is intended to provide or is related to treatment of the patient.
	"""
	
	education = "education"
	""" The activity is intended to provide or is related to education of the patient.
	"""
	
	assessment = "assessment"
	""" The activity is intended to perform or is related to assessment of the patient.
	"""
}


class AddressType(object) {
	""" The type of an address (physical / postal).

	URL: http://hl7.org/fhir/address-type
	ValueSet: http://hl7.org/fhir/ValueSet/address-type
	"""
	
	postal = "postal"
	""" Mailing addresses - PO Boxes and care-of addresses.
	"""
	
	physical = "physical"
	""" A physical address that can be visited.
	"""
	
	both = "both"
	""" An address that is both physical and postal.
	"""
}


class AddressUse(object) {
	""" The use of an address.

	URL: http://hl7.org/fhir/address-use
	ValueSet: http://hl7.org/fhir/ValueSet/address-use
	"""
	
	home = "home"
	""" A communication address at a home.
	"""
	
	work = "work"
	""" An office address. First choice for business related contacts during business hours.
	"""
	
	temp = "temp"
	""" A temporary address. The period can provide more detailed information.
	"""
	
	old = "old"
	""" This address is no longer in use (or was never correct but retained for records).
	"""
	
	billing = "billing"
	""" An address to be used to send bills, invoices, receipts etc.
	"""
}


class AdministrativeGender(object) {
	""" The gender of a person used for administrative purposes.

	URL: http://hl7.org/fhir/administrative-gender
	ValueSet: http://hl7.org/fhir/ValueSet/administrative-gender
	"""
	
	male = "male"
	""" Male.
	"""
	
	female = "female"
	""" Female.
	"""
	
	other = "other"
	""" Other.
	"""
	
	unknown = "unknown"
	""" Unknown.
	"""
}


class AdverseEventActuality(object) {
	""" Overall nature of the event, e.g. real or potential.

	URL: http://hl7.org/fhir/adverse-event-actuality
	ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-actuality
	"""
	
	actual = "actual"
	""" actual
	"""
	
	potential = "potential"
	""" potential
	"""
}


class AdverseEventCategory(object) {
	""" Overall categorization of the event, e.g. product related or situational.

	URL: http://terminology.hl7.org/CodeSystem/adverse-event-category
	ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-category
	"""
	
	productProblem = "product-problem"
	""" productProblem
	"""
	
	productQuality = "product-quality"
	""" productQuality
	"""
	
	productUseError = "product-use-error"
	""" productUseError
	"""
	
	wrongDose = "wrong-dose"
	""" wrongDose
	"""
	
	incorrectPrescribingInformation = "incorrect-prescribing-information"
	""" incorrectPrescribingInformation
	"""
	
	wrongTechnique = "wrong-technique"
	""" wrongTechnique
	"""
	
	wrongRouteOfAdministration = "wrong-route-of-administration"
	""" wrongRouteOfAdministration
	"""
	
	wrongRate = "wrong-rate"
	""" wrongRate
	"""
	
	wrongDuration = "wrong-duration"
	""" wrongDuration
	"""
	
	wrongTime = "wrong-time"
	""" wrongTime
	"""
	
	expiredDrug = "expired-drug"
	""" expiredDrug
	"""
	
	medicalDeviceUseError = "medical-device-use-error"
	""" medicalDeviceUseError
	"""
	
	problemDifferentManufacturer = "problem-different-manufacturer"
	""" problemDifferentManufacturer
	"""
	
	unsafePhysicalEnvironment = "unsafe-physical-environment"
	""" unsafePhysicalEnvironment
	"""
}


class AdverseEventCausalityAssessment(object) {
	""" TODO.

	URL: http://terminology.hl7.org/CodeSystem/adverse-event-causality-assess
	ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-causality-assess
	"""
	
	certain = "Certain"
	""" i) Event or laboratory test abnormality, with plausible time relationship to drug intake ii) Cannot be explained
	/// by disease or other drugs iii) Response to withdrawal plausible (pharmacologically, pathologically) iv) Event
	/// definitive pharmacologically or phenomenologically (i.e. an objective and specific medical disorder or a
	/// recognized pharmacological phenomenon) v) Re-challenge satisfactory, if necessary.
	"""
	
	probablyLikely = "Probably-Likely"
	""" i) Event or laboratory test abnormality, with reasonable time relationship to drug intake ii) Unlikely to be
	/// attributed to disease or other drugs iii) Response to withdrawal clinically reasonable iv) Re-challenge not
	/// required.
	"""
	
	possible = "Possible"
	""" i) Event or laboratory test abnormality, with reasonable time relationship to drug intake ii) Could also be
	/// explained by disease or other drugs iii) Information on drug withdrawal may be lacking or unclear.
	"""
	
	unlikely = "Unlikely"
	""" i) Event or laboratory test abnormality, with a time to drug intake that makes a relationship improbable (but
	/// not impossible) ii) Disease or other drugs provide plausible explanations.
	"""
	
	conditionalClassified = "Conditional-Classified"
	""" i) Event or laboratory test abnormality ii) More data for proper assessment needed, or iii) Additional data
	/// under examination.
	"""
	
	unassessableUnclassifiable = "Unassessable-Unclassifiable"
	""" i) Report suggesting an adverse reaction ii) Cannot be judged because information is insufficient or
	/// contradictory iii) Data cannot be supplemented or verified.
	"""
}


class AdverseEventCausalityMethod(object) {
	""" TODO.

	URL: http://terminology.hl7.org/CodeSystem/adverse-event-causality-method
	ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-causality-method
	"""
	
	probabilityScale = "ProbabilityScale"
	""" probabilityScale
	"""
	
	bayesian = "Bayesian"
	""" bayesian
	"""
	
	checklist = "Checklist"
	""" checklist
	"""
}


class AdverseEventOutcome(object) {
	""" TODO (and should this be required?).

	URL: http://terminology.hl7.org/CodeSystem/adverse-event-outcome
	ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-outcome
	"""
	
	resolved = "resolved"
	""" resolved
	"""
	
	recovering = "recovering"
	""" recovering
	"""
	
	ongoing = "ongoing"
	""" ongoing
	"""
	
	resolvedWithSequelae = "resolvedWithSequelae"
	""" resolvedWithSequelae
	"""
	
	fatal = "fatal"
	""" fatal
	"""
	
	unknown = "unknown"
	""" unknown
	"""
}


class AdverseEventSeriousness(object) {
	""" Overall seriousness of this event for the patient.

	URL: http://terminology.hl7.org/CodeSystem/adverse-event-seriousness
	ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-seriousness
	"""
	
	nonSerious = "Non-serious"
	""" Non-serious.
	"""
	
	serious = "Serious"
	""" Serious.
	"""
	
	seriousResultsInDeath = "SeriousResultsInDeath"
	""" Results in death.
	"""
	
	seriousIsLifeThreatening = "SeriousIsLifeThreatening"
	""" Is Life-threatening.
	"""
	
	seriousResultsInHospitalization = "SeriousResultsInHospitalization"
	""" Requires inpatient hospitalization or causes prolongation of existing hospitalization.
	"""
	
	seriousResultsInDisability = "SeriousResultsInDisability"
	""" Results in persistent or significant disability/incapacity.
	"""
	
	seriousIsBirthDefect = "SeriousIsBirthDefect"
	""" Is a congenital anomaly/birth defect.
	"""
	
	seriousRequiresPreventImpairment = "SeriousRequiresPreventImpairment"
	""" Requires intervention to prevent permanent impairment or damage (i.e., an important medical event that requires
	/// medical judgement).
	"""
}


class AdverseEventSeverity(object) {
	""" The severity of the adverse event itself, in direct relation to the subject.

	URL: http://terminology.hl7.org/CodeSystem/adverse-event-severity
	ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-severity
	"""
	
	mild = "mild"
	""" mild
	"""
	
	moderate = "moderate"
	""" moderate
	"""
	
	severe = "severe"
	""" severe
	"""
}


class AggregationMode(object) {
	""" How resource references can be aggregated.

	URL: http://hl7.org/fhir/resource-aggregation-mode
	ValueSet: http://hl7.org/fhir/ValueSet/resource-aggregation-mode
	"""
	
	contained = "contained"
	""" The reference is a local reference to a contained resource.
	"""
	
	referenced = "referenced"
	""" The reference to a resource that has to be resolved externally to the resource that includes the reference.
	"""
	
	bundled = "bundled"
	""" The resource the reference points to will be found in the same bundle as the resource that includes the
	/// reference.
	"""
}


class AllergyIntoleranceCategory(object) {
	""" Category of an identified substance.

	URL: http://hl7.org/fhir/allergy-intolerance-category
	ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-category
	"""
	
	food = "food"
	""" Any substance consumed to provide nutritional support for the body.
	"""
	
	medication = "medication"
	""" Substances administered to achieve a physiological effect.
	"""
	
	environment = "environment"
	""" Any substances that are encountered in the environment, including any substance not already classified as food,
	/// medication, or biologic.
	"""
	
	biologic = "biologic"
	""" A preparation that is synthesized from living organisms or their products, especially a human or animal protein,
	/// such as a hormone or antitoxin, that is used as a diagnostic, preventive, or therapeutic agent. Examples of
	/// biologic medications include: vaccines; allergenic extracts, which are used for both diagnosis and treatment
	/// (for example, allergy shots); gene therapies; cellular therapies.  There are other biologic products, such as
	/// tissues, that are not typically associated with allergies.
	"""
}


class AllergyIntoleranceCertainty(object) {
	""" Statement about the degree of clinical certainty that a specific substance was the cause of the manifestation in a
reaction event.

	URL: http://terminology.hl7.org/CodeSystem/reaction-event-certainty
	ValueSet: http://hl7.org/fhir/ValueSet/reaction-event-certainty
	"""
	
	unlikely = "unlikely"
	""" There is a low level of clinical certainty that the reaction was caused by the identified substance.
	"""
	
	likely = "likely"
	""" There is a high level of clinical certainty that the reaction was caused by the identified substance.
	"""
	
	confirmed = "confirmed"
	""" There is a very high level of clinical certainty that the reaction was due to the identified substance, which
	/// may include clinical evidence by testing or rechallenge.
	"""
	
	unknown = "unknown"
	""" The clinical certainty that the reaction was caused by the identified substance is unknown.  It is an explicit
	/// assertion that certainty is not known.
	"""
}


class AllergyIntoleranceCriticality(object) {
	""" Estimate of the potential clinical harm, or seriousness, of a reaction to an identified substance.

	URL: http://hl7.org/fhir/allergy-intolerance-criticality
	ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-criticality
	"""
	
	low = "low"
	""" Worst case result of a future exposure is not assessed to be life-threatening or having high potential for organ
	/// system failure.
	"""
	
	high = "high"
	""" Worst case result of a future exposure is assessed to be life-threatening or having high potential for organ
	/// system failure.
	"""
	
	unableToAssess = "unable-to-assess"
	""" Unable to assess the worst case result of a future exposure.
	"""
}


class AllergyIntoleranceSeverity(object) {
	""" Clinical assessment of the severity of a reaction event as a whole, potentially considering multiple different
manifestations.

	URL: http://hl7.org/fhir/reaction-event-severity
	ValueSet: http://hl7.org/fhir/ValueSet/reaction-event-severity
	"""
	
	mild = "mild"
	""" Causes mild physiological effects.
	"""
	
	moderate = "moderate"
	""" Causes moderate physiological effects.
	"""
	
	severe = "severe"
	""" Causes severe physiological effects.
	"""
}


class AllergyIntoleranceSubstanceExposureRisk(object) {
	""" The risk of an adverse reaction (allergy or intolerance) for this patient upon exposure to the substance (including
pharmaceutical products).

	URL: http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk
	ValueSet: http://hl7.org/fhir/ValueSet/allerg-intol-substance-exp-risk
	"""
	
	knownReactionRisk = "known-reaction-risk"
	""" Known risk of allergy or intolerance reaction upon exposure to the specified substance.
	"""
	
	noKnownReactionRisk = "no-known-reaction-risk"
	""" No known risk of allergy or intolerance reaction upon exposure to the specified substance.
	"""
}


class AllergyIntoleranceType(object) {
	""" Identification of the underlying physiological mechanism for a Reaction Risk.

	URL: http://hl7.org/fhir/allergy-intolerance-type
	ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-type
	"""
	
	allergy = "allergy"
	""" A propensity for hypersensitivity reaction(s) to a substance.  These reactions are most typically type I
	/// hypersensitivity, plus other "allergy-like" reactions, including pseudoallergy.
	"""
	
	intolerance = "intolerance"
	""" A propensity for adverse reactions to a substance that is not judged to be allergic or "allergy-like".  These
	/// reactions are typically (but not necessarily) non-immune.  They are to some degree idiosyncratic and/or
	/// individually specific (i.e. are not a reaction that is expected to occur with most or all patients given similar
	/// circumstances).
	"""
}


class AlternativeCodeKind(object) {
	""" Indicates the type of use for which the code is defined.

	URL: http://terminology.hl7.org/CodeSystem/composition-altcode-kind
	ValueSet: http://hl7.org/fhir/ValueSet/composition-altcode-kind
	"""
	
	alternate = "alternate"
	""" The code is an alternative code that can be used in any of the circumstances that the primary code can be used.
	"""
	
	deprecated = "deprecated"
	""" The code should no longer be used, but was used in the past.
	"""
	
	caseInsensitive = "case-insensitive"
	""" The code is an alternative to be used when a case insensitive code is required (when the primary codes are case
	/// sensitive).
	"""
	
	caseSensitive = "case-sensitive"
	""" The code is an alternative to be used when a case sensitive code is required (when the primary codes are case
	/// insensitive).
	"""
	
	expression = "expression"
	""" The code is an alternative for the primary code that is built using the expression grammar defined by the code
	/// system.
	"""
}


class AlternativeCodeKind(object) {
	""" Indicates the type of use for which the code is defined.

	URL: http://terminology.hl7.org/CodeSystem/codesystem-altcode-kind
	ValueSet: http://hl7.org/fhir/ValueSet/codesystem-altcode-kind
	"""
	
	alternate = "alternate"
	""" The code is an alternative code that can be used in any of the circumstances that the primary code can be used.
	"""
	
	deprecated = "deprecated"
	""" The code should no longer be used, but was used in the past.
	"""
	
	caseInsensitive = "case-insensitive"
	""" The code is an alternative to be used when a case insensitive code is required (when the primary codes are case
	/// sensitive).
	"""
	
	caseSensitive = "case-sensitive"
	""" The code is an alternative to be used when a case sensitive code is required (when the primary codes are case
	/// insensitive).
	"""
	
	expression = "expression"
	""" The code is an alternative for the primary code that is built using the expression grammar defined by the code
	/// system.
	"""
}


class AppointmentStatus(object) {
	""" The free/busy status of an appointment.

	URL: http://hl7.org/fhir/appointmentstatus
	ValueSet: http://hl7.org/fhir/ValueSet/appointmentstatus
	"""
	
	proposed = "proposed"
	""" None of the participant(s) have finalized their acceptance of the appointment request, and the start/end time
	/// might not be set yet.
	"""
	
	pending = "pending"
	""" Some or all of the participant(s) have not finalized their acceptance of the appointment request.
	"""
	
	booked = "booked"
	""" All participant(s) have been considered and the appointment is confirmed to go ahead at the date/times
	/// specified.
	"""
	
	arrived = "arrived"
	""" The patient/patients has/have arrived and is/are waiting to be seen.
	"""
	
	fulfilled = "fulfilled"
	""" This appointment has completed and may have resulted in an encounter.
	"""
	
	cancelled = "cancelled"
	""" The appointment has been cancelled.
	"""
	
	noshow = "noshow"
	""" Some or all of the participant(s) have not/did not appear for the appointment (usually the patient).
	"""
	
	enteredInError = "entered-in-error"
	""" This instance should not have been part of this patient's medical record.
	"""
	
	checkedIn = "checked-in"
	""" When checked in, all pre-encounter administrative work is complete, and the encounter may begin. (where multiple
	/// patients are involved, they are all present).
	"""
	
	waitlist = "waitlist"
	""" The appointment has been placed on a waitlist, to be scheduled/confirmed in the future when a slot/service is
	/// available.
	/// A specific time might or might not be pre-allocated.
	"""
}


class AssertionDirectionType(object) {
	""" The type of direction to use for assertion.

	URL: http://hl7.org/fhir/assert-direction-codes
	ValueSet: http://hl7.org/fhir/ValueSet/assert-direction-codes
	"""
	
	response = "response"
	""" The assertion is evaluated on the response. This is the default value.
	"""
	
	request = "request"
	""" The assertion is evaluated on the request.
	"""
}


class AssertionOperatorType(object) {
	""" The type of operator to use for assertion.

	URL: http://hl7.org/fhir/assert-operator-codes
	ValueSet: http://hl7.org/fhir/ValueSet/assert-operator-codes
	"""
	
	equals = "equals"
	""" Default value. Equals comparison.
	"""
	
	notEquals = "notEquals"
	""" Not equals comparison.
	"""
	
	in = "in"
	""" Compare value within a known set of values.
	"""
	
	notIn = "notIn"
	""" Compare value not within a known set of values.
	"""
	
	greaterThan = "greaterThan"
	""" Compare value to be greater than a known value.
	"""
	
	lessThan = "lessThan"
	""" Compare value to be less than a known value.
	"""
	
	empty = "empty"
	""" Compare value is empty.
	"""
	
	notEmpty = "notEmpty"
	""" Compare value is not empty.
	"""
	
	contains = "contains"
	""" Compare value string contains a known value.
	"""
	
	notContains = "notContains"
	""" Compare value string does not contain a known value.
	"""
	
	eval = "eval"
	""" Evaluate the FHIRPath expression as a boolean condition.
	"""
}


class AssertionResponseTypes(object) {
	""" The type of response code to use for assertion.

	URL: http://hl7.org/fhir/assert-response-code-types
	ValueSet: http://hl7.org/fhir/ValueSet/assert-response-code-types
	"""
	
	okay = "okay"
	""" Response code is 200.
	"""
	
	created = "created"
	""" Response code is 201.
	"""
	
	noContent = "noContent"
	""" Response code is 204.
	"""
	
	notModified = "notModified"
	""" Response code is 304.
	"""
	
	bad = "bad"
	""" Response code is 400.
	"""
	
	forbidden = "forbidden"
	""" Response code is 403.
	"""
	
	notFound = "notFound"
	""" Response code is 404.
	"""
	
	methodNotAllowed = "methodNotAllowed"
	""" Response code is 405.
	"""
	
	conflict = "conflict"
	""" Response code is 409.
	"""
	
	gone = "gone"
	""" Response code is 410.
	"""
	
	preconditionFailed = "preconditionFailed"
	""" Response code is 412.
	"""
	
	unprocessable = "unprocessable"
	""" Response code is 422.
	"""
}


class AuditEventAction(object) {
	""" Indicator for type of action performed during the event that generated the event.

	URL: http://hl7.org/fhir/audit-event-action
	ValueSet: http://hl7.org/fhir/ValueSet/audit-event-action
	"""
	
	C = "C"
	""" Create a new database object, such as placing an order.
	"""
	
	R = "R"
	""" Display or print data, such as a doctor census.
	"""
	
	U = "U"
	""" Update data, such as revise patient information.
	"""
	
	D = "D"
	""" Delete items, such as a doctor master file record.
	"""
	
	E = "E"
	""" Perform a system or application function such as log-on, program execution or use of an object's method, or
	/// perform a query/search operation.
	"""
}


class BindingStrength(object) {
	""" Indication of the degree of conformance expectations associated with a binding.

	URL: http://hl7.org/fhir/binding-strength
	ValueSet: http://hl7.org/fhir/ValueSet/binding-strength
	"""
	
	required = "required"
	""" To be conformant, the concept in this element SHALL be from the specified value set.
	"""
	
	extensible = "extensible"
	""" To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within
	/// the value set can apply to the concept being communicated.  If the value set does not cover the concept (based
	/// on human review), alternate codings (or, data type allowing, text) may be included instead.
	"""
	
	preferred = "preferred"
	""" Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to
	/// do so to be considered conformant.
	"""
	
	example = "example"
	""" Instances are not expected or even encouraged to draw from the specified value set.  The value set merely
	/// provides examples of the types of concepts intended to be included.
	"""
}


class BiologicallyDerivedProductCategory(object) {
	""" Biologically Derived Product Category.

	URL: http://hl7.org/fhir/product-category
	ValueSet: http://hl7.org/fhir/ValueSet/product-category
	"""
	
	organ = "organ"
	""" A collection of tissues joined in a structural unit to serve a common function.
	"""
	
	tissue = "tissue"
	""" An ensemble of similar cells and their extracellular matrix from the same origin that together carry out a
	/// specific function.
	"""
	
	fluid = "fluid"
	""" Body fluid.
	"""
	
	cells = "cells"
	""" Collection of cells.
	"""
	
	biologicalAgent = "biologicalAgent"
	""" Biological agent of unspecified type.
	"""
}


class BiologicallyDerivedProductStatus(object) {
	""" Biologically Derived Product Status.

	URL: http://hl7.org/fhir/product-status
	ValueSet: http://hl7.org/fhir/ValueSet/product-status
	"""
	
	available = "available"
	""" Product is currently available for use.
	"""
	
	unavailable = "unavailable"
	""" Product is not currently available for use.
	"""
}


class BiologicallyDerivedProductStorageScale(object) {
	""" BiologicallyDerived Product Storage Scale.

	URL: http://hl7.org/fhir/product-storage-scale
	ValueSet: http://hl7.org/fhir/ValueSet/product-storage-scale
	"""
	
	farenheit = "farenheit"
	""" Fahrenheit temperature scale.
	"""
	
	celsius = "celsius"
	""" Celsius or centigrade temperature scale.
	"""
	
	kelvin = "kelvin"
	""" Kelvin absolute thermodynamic temperature scale.
	"""
}


class BundleType(object) {
	""" Indicates the purpose of a bundle - how it is intended to be used.

	URL: http://hl7.org/fhir/bundle-type
	ValueSet: http://hl7.org/fhir/ValueSet/bundle-type
	"""
	
	document = "document"
	""" The bundle is a document. The first resource is a Composition.
	"""
	
	message = "message"
	""" The bundle is a message. The first resource is a MessageHeader.
	"""
	
	transaction = "transaction"
	""" The bundle is a transaction - intended to be processed by a server as an atomic commit.
	"""
	
	transactionResponse = "transaction-response"
	""" The bundle is a transaction response. Because the response is a transaction response, the transaction has
	/// succeeded, and all responses are error free.
	"""
	
	batch = "batch"
	""" The bundle is a set of actions - intended to be processed by a server as a group of independent actions.
	"""
	
	batchResponse = "batch-response"
	""" The bundle is a batch response. Note that as a batch, some responses may indicate failure and others success.
	"""
	
	history = "history"
	""" The bundle is a list of resources from a history interaction on a server.
	"""
	
	searchset = "searchset"
	""" The bundle is a list of resources returned as a result of a search/query interaction, operation, or message.
	"""
	
	collection = "collection"
	""" The bundle is a set of resources collected into a single package for ease of distribution that imposes no
	/// processing obligations or behavioral rules beyond persistence.
	"""
}


class CanonicalStatusCodesForFHIRResources(object) {
	""" The master set of status codes used throughout FHIR. All status codes are mapped to one of these codes.

	URL: http://hl7.org/fhir/resource-status
	ValueSet: http://hl7.org/fhir/ValueSet/resource-status
	"""
	
	error = "error"
	""" The resource was created in error, and should not be treated as valid (note: in many cases, for various data
	/// integrity related reasons, the information cannot be removed from the record)
	"""
	
	proposed = "proposed"
	""" The resource describes an action or plan that is proposed, and not yet approved by the participants
	"""
	
	planned = "planned"
	""" The resource describes a course of action that is planned and agreed/approved, but at the time of recording was
	/// still future
	"""
	
	draft = "draft"
	""" The information in the resource is still being prepared and edited
	"""
	
	requested = "requested"
	""" A fulfiller has been asked to perform this action, but it has not yet occurred
	"""
	
	received = "received"
	""" The fulfiller has received the request, but not yet agreed to carry out the action
	"""
	
	declined = "declined"
	""" The fulfiller chose not to perform the action
	"""
	
	accepted = "accepted"
	""" The fulfiller has decided to perform the action, and plans are in train to do this in the future
	"""
	
	arrived = "arrived"
	""" The pre-conditions for the action are all fulfilled, and it is imminent
	"""
	
	active = "active"
	""" The resource describes information that is currently valid or a process that is presently occuring
	"""
	
	suspended = "suspended"
	""" The process described/requested in this resource has been halted for some reason
	"""
	
	failed = "failed"
	""" The process described/requested in the resource could not be completed, and no further action is planned
	"""
	
	replaced = "replaced"
	""" The information in this resource has been replaced by information in another resource
	"""
	
	complete = "complete"
	""" The process described/requested in the resource has been completed, and no further action is planned
	"""
	
	inactive = "inactive"
	""" The resource describes information that is no longer valid or a process that is stopped occurring
	"""
	
	abandoned = "abandoned"
	""" The process described/requested in the resource did not complete - usually due to some workflow error, and no
	/// further action is planned
	"""
	
	unknown = "unknown"
	""" Authoring system does not know the status
	"""
	
	unconfirmed = "unconfirmed"
	""" The information in this resource is not yet approved
	"""
	
	confirmed = "confirmed"
	""" The information in this resource is approved
	"""
	
	resolved = "resolved"
	""" The issue identified by this resource is no longer of concern
	"""
	
	refuted = "refuted"
	""" This information has been ruled out by testing and evaluation
	"""
	
	differential = "differential"
	""" Potentially true?
	"""
	
	partial = "partial"
	""" This information is still being assembled
	"""
	
	busyUnavailable = "busy-unavailable"
	""" not available at this time/location
	"""
	
	free = "free"
	""" Free for scheduling
	"""
	
	onTarget = "on-target"
	""" Ready to act
	"""
	
	aheadOfTarget = "ahead-of-target"
	""" Ahead of the planned timelines
	"""
	
	behindTarget = "behind-target"
	""" behindTarget
	"""
	
	notReady = "not-ready"
	""" Behind the planned timelines
	"""
	
	transducDiscon = "transduc-discon"
	""" The device transducer is disconnected
	"""
	
	hwDiscon = "hw-discon"
	""" The hardware is disconnected
	"""
}


class CapabilityStatementKind(object) {
	""" How a capability statement is intended to be used.

	URL: http://hl7.org/fhir/capability-statement-kind
	ValueSet: http://hl7.org/fhir/ValueSet/capability-statement-kind
	"""
	
	instance = "instance"
	""" The CapabilityStatement instance represents the present capabilities of a specific system instance.  This is the
	/// kind returned by /metadata for a FHIR server end-point.
	"""
	
	capability = "capability"
	""" The CapabilityStatement instance represents the capabilities of a system or piece of software, independent of a
	/// particular installation.
	"""
	
	requirements = "requirements"
	""" The CapabilityStatement instance represents a set of requirements for other systems to meet; e.g. as part of an
	/// implementation guide or 'request for proposal'.
	"""
}


class CarePlanActivityStatus(object) {
	""" Indicates where the activity is at in its overall life cycle.

	URL: http://hl7.org/fhir/care-plan-activity-status
	ValueSet: http://hl7.org/fhir/ValueSet/care-plan-activity-status
	"""
	
	notStarted = "not-started"
	""" Activity is planned but no action has yet been taken.
	"""
	
	scheduled = "scheduled"
	""" Appointment or other booking has occurred but activity has not yet begun.
	"""
	
	inProgress = "in-progress"
	""" Activity has been started but is not yet complete.
	"""
	
	onHold = "on-hold"
	""" Activity was started but has temporarily ceased with an expectation of resumption at a future time.
	"""
	
	completed = "completed"
	""" The activity has been completed (more or less) as planned.
	"""
	
	cancelled = "cancelled"
	""" The planned activity has been withdrawn.
	"""
	
	stopped = "stopped"
	""" The planned activity has been ended prior to completion after the activity was started.
	"""
	
	unknown = "unknown"
	""" The current state of the activity is not known.  Note: This concept is not to be used for "other".
	"""
	
	enteredInError = "entered-in-error"
	""" The activity was entered in error and voided.
	"""
}


class CareTeamStatus(object) {
	""" Indicates the status of the care team.

	URL: http://hl7.org/fhir/care-team-status
	ValueSet: http://hl7.org/fhir/ValueSet/care-team-status
	"""
	
	proposed = "proposed"
	""" The care team has been drafted and proposed, but not yet participating in the coordination and delivery of care.
	"""
	
	active = "active"
	""" The care team is currently participating in the coordination and delivery of care.
	"""
	
	suspended = "suspended"
	""" The care team is temporarily on hold or suspended and not participating in the coordination and delivery of
	/// care.
	"""
	
	inactive = "inactive"
	""" The care team was, but is no longer, participating in the coordination and delivery of care.
	"""
	
	enteredInError = "entered-in-error"
	""" The care team should have never existed.
	"""
}


class CatalogEntryRelationType(object) {
	""" The type of relations between entries.

	URL: http://hl7.org/fhir/relation-type
	ValueSet: http://hl7.org/fhir/ValueSet/relation-type
	"""
	
	triggers = "triggers"
	""" the related entry represents an activity that may be triggered by the current item.
	"""
	
	isReplacedBy = "is-replaced-by"
	""" the related entry represents an item that replaces the current retired item.
	"""
}


class CatalogType(object) {
	""" The type of catalog.

	URL: http://terminology.hl7.org/CodeSystem/catalogType
	ValueSet: http://hl7.org/fhir/ValueSet/catalogType
	"""
	
	medication = "medication"
	""" Medication Catalog.
	"""
	
	device = "device"
	""" Device Catalog.
	"""
	
	protocol = "protocol"
	""" Protocol List.
	"""
}


class CertaintySubcomponentRating(object) {
	""" The quality rating of the subcomponent of a quality of evidence rating.

	URL: http://terminology.hl7.org/CodeSystem/certainty-subcomponent-rating
	ValueSet: http://hl7.org/fhir/ValueSet/certainty-subcomponent-rating
	"""
	
	noChange = "no-change"
	""" no change to quality rating.
	"""
	
	downcode1 = "downcode1"
	""" reduce quality rating by 1.
	"""
	
	downcode2 = "downcode2"
	""" reduce quality rating by 2.
	"""
	
	downcode3 = "downcode3"
	""" reduce quality rating by 3.
	"""
	
	upcode1 = "upcode1"
	""" increase quality rating by 1.
	"""
	
	upcode2 = "upcode2"
	""" increase quality rating by 2.
	"""
	
	noConcern = "no-concern"
	""" no serious concern.
	"""
	
	seriousConcern = "serious-concern"
	""" serious concern.
	"""
	
	criticalConcern = "critical-concern"
	""" critical concern.
	"""
	
	present = "present"
	""" possible reason for increasing quality rating was checked and found to bepresent.
	"""
	
	absent = "absent"
	""" possible reason for increasing quality rating was checked and found to be absent.
	"""
}


class CertaintySubcomponentType(object) {
	""" The subcomponent classification of quality of evidence rating systems.

	URL: http://terminology.hl7.org/CodeSystem/certainty-subcomponent-type
	ValueSet: http://hl7.org/fhir/ValueSet/certainty-subcomponent-type
	"""
	
	riskOfBias = "RiskOfBias"
	""" methodologic concerns reducing internal validity.
	"""
	
	inconsistency = "Inconsistency"
	""" concerns that findings are not similar enough to support certainty.
	"""
	
	indirectness = "Indirectness"
	""" concerns reducing external validity.
	"""
	
	imprecision = "Imprecision"
	""" High quality evidence.
	"""
	
	publicationBias = "PublicationBias"
	""" likelihood that what is published misrepresents what is available to publish.
	"""
	
	doseResponseGradient = "DoseResponseGradient"
	""" higher certainty due to dose response relationship.
	"""
	
	plausibleConfounding = "PlausibleConfounding"
	""" higher certainty due to risk of bias in opposite direction.
	"""
	
	largeEffect = "LargeEffect"
	""" higher certainty due to large effect size.
	"""
}


class ChargeItemStatus(object) {
	""" Codes identifying the lifecycle stage of a ChargeItem.

	URL: http://hl7.org/fhir/chargeitem-status
	ValueSet: http://hl7.org/fhir/ValueSet/chargeitem-status
	"""
	
	planned = "planned"
	""" The charge item has been entered, but the charged service is not  yet complete, so it shall not be billed yet
	/// but might be used in the context of pre-authorization.
	"""
	
	billable = "billable"
	""" The charge item is ready for billing.
	"""
	
	notBillable = "not-billable"
	""" The charge item has been determined to be not billable (e.g. due to rules associated with the billing code).
	"""
	
	aborted = "aborted"
	""" The processing of the charge was aborted.
	"""
	
	billed = "billed"
	""" The charge item has been billed (e.g. a billing engine has generated financial transactions by applying the
	/// associated ruled for the charge item to the context of the Encounter, and placed them into Claims/Invoices.
	"""
	
	enteredInError = "entered-in-error"
	""" The charge item has been entered in error and should not be processed for billing.
	"""
	
	unknown = "unknown"
	""" The authoring system does not know which of the status values currently applies for this charge item  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
	"""
}


class ChoiceListOrientation(object) {
	""" Direction in which lists of possible answers should be displayed.

	URL: http://terminology.hl7.org/CodeSystem/choice-list-orientation
	ValueSet: http://hl7.org/fhir/ValueSet/choice-list-orientation
	"""
	
	horizontal = "horizontal"
	""" List choices along the horizontal axis.
	"""
	
	vertical = "vertical"
	""" List choices down the vertical axis.
	"""
}


class ClaimPayeeResourceType(object) {
	""" The type of Claim payee Resource.

	URL: http://terminology.hl7.org/CodeSystem/ex-payee-resource-type
	ValueSet: http://hl7.org/fhir/ValueSet/ex-payee-resource-type
	"""
	
	organization = "organization"
	""" Organization resource.
	"""
	
	patient = "patient"
	""" Patient resource.
	"""
	
	practitioner = "practitioner"
	""" Practitioner resource.
	"""
	
	relatedperson = "relatedperson"
	""" RelatedPerson resource.
	"""
}


class CodeSearchSupport(object) {
	""" The degree to which the server supports the code search parameter on ValueSet, if it is supported.

	URL: http://hl7.org/fhir/code-search-support
	ValueSet: http://hl7.org/fhir/ValueSet/code-search-support
	"""
	
	explicit = "explicit"
	""" The search for code on ValueSet only includes codes explicitly detailed on includes or expansions.
	"""
	
	all = "all"
	""" The search for code on ValueSet only includes all codes based on the expansion of the value set.
	"""
}


class CodeSystemContentMode(object) {
	""" The extent of the content of the code system (the concepts and codes it defines) are represented in a code system
resource.

	URL: http://hl7.org/fhir/codesystem-content-mode
	ValueSet: http://hl7.org/fhir/ValueSet/codesystem-content-mode
	"""
	
	notPresent = "not-present"
	""" None of the concepts defined by the code system are included in the code system resource.
	"""
	
	example = "example"
	""" A few representative concepts are included in the code system resource. There is no useful intent in the subset
	/// choice and there's no process to make it workable: it's not intended to be workable.
	"""
	
	fragment = "fragment"
	""" A subset of the code system concepts are included in the code system resource. This is a curated subset released
	/// for a specific purpose under the governance of the code system steward, and that the intent, bounds and
	/// consequences of the fragmentation are clearly defined in the fragment or the code system documentation.
	/// Fragments are also known as partitions.
	"""
	
	complete = "complete"
	""" All the concepts defined by the code system are included in the code system resource.
	"""
	
	supplement = "supplement"
	""" The resource doesn't define any new concepts; it just provides additional designations and properties to another
	/// code system.
	"""
}


class CodeSystemHierarchyMeaning(object) {
	""" The meaning of the hierarchy of concepts in a code system.

	URL: http://hl7.org/fhir/codesystem-hierarchy-meaning
	ValueSet: http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning
	"""
	
	groupedBy = "grouped-by"
	""" No particular relationship between the concepts can be assumed, except what can be determined by inspection of
	/// the definitions of the elements (possible reasons to use this: importing from a source where this is not
	/// defined, or where various parts of the hierarchy have different meanings).
	"""
	
	isA = "is-a"
	""" A hierarchy where the child concepts have an IS-A relationship with the parents - that is, all the properties of
	/// the parent are also true for its child concepts. Not that is-a is a property of the concepts, so additional
	/// subsumption relationships may be defined using properties or the [subsumes](extension-codesystem-subsumes.html)
	/// extension.
	"""
	
	partOf = "part-of"
	""" Child elements list the individual parts of a composite whole (e.g. body site).
	"""
	
	classifiedWith = "classified-with"
	""" Child concepts in the hierarchy may have only one parent, and there is a presumption that the code system is a
	/// "closed world" meaning all things must be in the hierarchy. This results in concepts such as "not otherwise
	/// classified.".
	"""
}


class CommunicationCategory(object) {
	""" Codes for general categories of communications such as alerts, instruction, etc.

	URL: http://terminology.hl7.org/CodeSystem/communication-category
	ValueSet: http://hl7.org/fhir/ValueSet/communication-category
	"""
	
	alert = "alert"
	""" The communication conveys an alert.
	"""
	
	notification = "notification"
	""" The communication conveys a notification.
	"""
	
	reminder = "reminder"
	""" The communication conveys a reminder.
	"""
	
	instruction = "instruction"
	""" The communication conveys instruction.
	"""
}


class CommunicationNotDoneReason(object) {
	""" Codes for the reason why a communication was not done.

	URL: http://terminology.hl7.org/CodeSystem/communication-not-done-reason
	ValueSet: http://hl7.org/fhir/ValueSet/communication-not-done-reason
	"""
	
	unknown = "unknown"
	""" The communication was not done due to an unknown reason.
	"""
	
	systemError = "system-error"
	""" The communication was not done due to a system error.
	"""
	
	invalidPhoneNumber = "invalid-phone-number"
	""" The communication was not done due to an invalid phone number.
	"""
	
	recipientUnavailable = "recipient-unavailable"
	""" The communication was not done due to the recipient being unavailable.
	"""
	
	familyObjection = "family-objection"
	""" The communication was not done due to a family objection.
	"""
	
	patientObjection = "patient-objection"
	""" The communication was not done due to a patient objection.
	"""
}


class CommunicationTopic(object) {
	""" Codes describing the purpose or content of the communication.

	URL: http://terminology.hl7.org/CodeSystem/communication-topic
	ValueSet: http://hl7.org/fhir/ValueSet/communication-topic
	"""
	
	prescriptionRefillRequest = "prescription-refill-request"
	""" The purpose of the communication is a prescription refill request.
	"""
	
	progressUpdate = "progress-update"
	""" The purpose of the communication is a progress update.
	"""
	
	reportLabs = "report-labs"
	""" The purpose of the communication is to report labs.
	"""
	
	appointmentReminder = "appointment-reminder"
	""" The purpose of the communication is an appointment reminder.
	"""
	
	phoneConsult = "phone-consult"
	""" The purpose of the communication is a phone consult.
	"""
	
	summaryReport = "summary-report"
	""" The purpose of the communication is a summary report.
	"""
}


class CompartmentType(object) {
	""" Which type a compartment definition describes.

	URL: http://hl7.org/fhir/compartment-type
	ValueSet: http://hl7.org/fhir/ValueSet/compartment-type
	"""
	
	patient = "Patient"
	""" The compartment definition is for the patient compartment.
	"""
	
	encounter = "Encounter"
	""" The compartment definition is for the encounter compartment.
	"""
	
	relatedPerson = "RelatedPerson"
	""" The compartment definition is for the related-person compartment.
	"""
	
	practitioner = "Practitioner"
	""" The compartment definition is for the practitioner compartment.
	"""
	
	device = "Device"
	""" The compartment definition is for the device compartment.
	"""
}


class CompositeMeasureScoring(object) {
	""" The composite scoring method of the measure.

	URL: http://terminology.hl7.org/CodeSystem/composite-measure-scoring
	ValueSet: http://hl7.org/fhir/ValueSet/composite-measure-scoring
	"""
	
	opportunity = "opportunity"
	""" Opportunity scoring combines the scores from component measures by combining the numerators and denominators for
	/// each component.
	"""
	
	allOrNothing = "all-or-nothing"
	""" All-or-nothing scoring includes an individual in the numerator of the composite measure if they are in the
	/// numerators of all of the component measures in which they are in the denominator.
	"""
	
	linear = "linear"
	""" Linear scoring gives an individual a score based on the number of numerators in which they appear.
	"""
	
	weighted = "weighted"
	""" Weighted scoring gives an individual a score based on a weighted factor for each component numerator in which
	/// they appear.
	"""
}


class CompositionAttestationMode(object) {
	""" The way in which a person authenticated a composition.

	URL: http://hl7.org/fhir/composition-attestation-mode
	ValueSet: http://hl7.org/fhir/ValueSet/composition-attestation-mode
	"""
	
	personal = "personal"
	""" The person authenticated the content in their personal capacity.
	"""
	
	professional = "professional"
	""" The person authenticated the content in their professional capacity.
	"""
	
	legal = "legal"
	""" The person authenticated the content and accepted legal responsibility for its content.
	"""
	
	official = "official"
	""" The organization authenticated the content as consistent with their policies and procedures.
	"""
}


class CompositionStatus(object) {
	""" The workflow/clinical status of the composition.

	URL: http://hl7.org/fhir/composition-status
	ValueSet: http://hl7.org/fhir/ValueSet/composition-status
	"""
	
	preliminary = "preliminary"
	""" This is a preliminary composition or document (also known as initial or interim). The content may be incomplete
	/// or unverified.
	"""
	
	final = "final"
	""" This version of the composition is complete and verified by an appropriate person and no further work is
	/// planned. Any subsequent updates would be on a new version of the composition.
	"""
	
	amended = "amended"
	""" The composition content or the referenced resources have been modified (edited or added to) subsequent to being
	/// released as "final" and the composition is complete and verified by an authorized person.
	"""
	
	enteredInError = "entered-in-error"
	""" The composition or document was originally created/issued in error, and this is an amendment that marks that the
	/// entire series should not be considered as valid.
	"""
}


class ConceptMapEquivalence(object) {
	""" The degree of equivalence between concepts.

	URL: http://hl7.org/fhir/concept-map-equivalence
	ValueSet: http://hl7.org/fhir/ValueSet/concept-map-equivalence
	"""
	
	relatedto = "relatedto"
	""" The concepts are related to each other, and have at least some overlap in meaning, but the exact relationship is
	/// not known.
	"""
	
	equivalent = "equivalent"
	""" The definitions of the concepts mean the same thing (including when structural implications of meaning are
	/// considered) (i.e. extensionally identical).
	"""
	
	equal = "equal"
	""" The definitions of the concepts are exactly the same (i.e. only grammatical differences) and structural
	/// implications of meaning are identical or irrelevant (i.e. intentionally identical).
	"""
	
	wider = "wider"
	""" The target mapping is wider in meaning than the source concept.
	"""
	
	subsumes = "subsumes"
	""" The target mapping subsumes the meaning of the source concept (e.g. the source is-a target).
	"""
	
	narrower = "narrower"
	""" The target mapping is narrower in meaning than the source concept. The sense in which the mapping is narrower
	/// SHALL be described in the comments in this case, and applications should be careful when attempting to use these
	/// mappings operationally.
	"""
	
	specializes = "specializes"
	""" The target mapping specializes the meaning of the source concept (e.g. the target is-a source).
	"""
	
	inexact = "inexact"
	""" The target mapping overlaps with the source concept, but both source and target cover additional meaning, or the
	/// definitions are imprecise and it is uncertain whether they have the same boundaries to their meaning. The sense
	/// in which the mapping is inexact SHALL be described in the comments in this case, and applications should be
	/// careful when attempting to use these mappings operationally.
	"""
	
	unmatched = "unmatched"
	""" There is no match for this concept in the target code system.
	"""
	
	disjoint = "disjoint"
	""" This is an explicit assertion that there is no mapping between the source and target concept.
	"""
}


class ConceptMapGroupUnmappedMode(object) {
	""" Defines which action to take if there is no match in the group.

	URL: http://hl7.org/fhir/conceptmap-unmapped-mode
	ValueSet: http://hl7.org/fhir/ValueSet/conceptmap-unmapped-mode
	"""
	
	provided = "provided"
	""" Use the code as provided in the $translate request.
	"""
	
	fixed = "fixed"
	""" Use the code explicitly provided in the group.unmapped.
	"""
	
	otherMap = "other-map"
	""" Use the map identified by the canonical URL in the url element.
	"""
}


class ConceptSubsumptionOutcome(object) {
	""" The subsumption relationship between code/Coding "A" and code/Coding "B". There are 4 possible codes to be returned:
equivalent, subsumes, subsumed-by, and not-subsumed. If the server is unable to determine the relationship between the
codes/Codings, then it returns an error (i.e. an OperationOutcome).

	URL: http://hl7.org/fhir/concept-subsumption-outcome
	ValueSet: http://hl7.org/fhir/ValueSet/concept-subsumption-outcome
	"""
	
	equivalent = "equivalent"
	""" The two concepts are equivalent (have the same properties).
	"""
	
	subsumes = "subsumes"
	""" Coding/code "A" subsumes Coding/code "B" (e.g. B has all the properties A has, and some of it's own).
	"""
	
	subsumedBy = "subsumed-by"
	""" Coding/code "A" is subsumed by Coding/code "B" (e.g. A has all the properties B has, and some of it's own).
	"""
	
	notSubsumed = "not-subsumed"
	""" Coding/code "A" and Coding/code "B" are disjoint (e.g. each has propeties that the other doesn't have).
	"""
}


class ConditionState(object) {
	""" Enumeration indicating whether the condition is currently active, inactive, or has been resolved.

	URL: http://terminology.hl7.org/CodeSystem/condition-state
	ValueSet: http://hl7.org/fhir/ValueSet/condition-state
	"""
	
	active = "active"
	""" The condition is active.
	"""
	
	inactive = "inactive"
	""" The condition is inactive, but not resolved.
	"""
	
	resolved = "resolved"
	""" The condition is resolved.
	"""
}


class ConditionVerificationStatus(object) {
	""" The verification status to support or decline the clinical status of the condition or diagnosis.

	URL: http://terminology.hl7.org/CodeSystem/condition-ver-status
	ValueSet: http://hl7.org/fhir/ValueSet/condition-ver-status
	"""
	
	unconfirmed = "unconfirmed"
	""" There is not sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
	"""
	
	provisional = "provisional"
	""" This is a tentative diagnosis - still a candidate that is under consideration.
	"""
	
	differential = "differential"
	""" One of a set of potential (and typically mutually exclusive) diagnoses asserted to further guide the diagnostic
	/// process and preliminary treatment.
	"""
	
	confirmed = "confirmed"
	""" There is sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
	"""
	
	refuted = "refuted"
	""" This condition has been ruled out by diagnostic and clinical evidence.
	"""
	
	enteredInError = "entered-in-error"
	""" The statement was entered in error and is not valid.
	"""
}


class ConditionalDeleteStatus(object) {
	""" A code that indicates how the server supports conditional delete.

	URL: http://hl7.org/fhir/conditional-delete-status
	ValueSet: http://hl7.org/fhir/ValueSet/conditional-delete-status
	"""
	
	notSupported = "not-supported"
	""" No support for conditional deletes.
	"""
	
	single = "single"
	""" Conditional deletes are supported, but only single resources at a time.
	"""
	
	multiple = "multiple"
	""" Conditional deletes are supported, and multiple resources can be deleted in a single interaction.
	"""
}


class ConditionalReadStatus(object) {
	""" A code that indicates how the server supports conditional read.

	URL: http://hl7.org/fhir/conditional-read-status
	ValueSet: http://hl7.org/fhir/ValueSet/conditional-read-status
	"""
	
	notSupported = "not-supported"
	""" No support for conditional reads.
	"""
	
	modifiedSince = "modified-since"
	""" Conditional reads are supported, but only with the If-Modified-Since HTTP Header.
	"""
	
	notMatch = "not-match"
	""" Conditional reads are supported, but only with the If-None-Match HTTP Header.
	"""
	
	fullSupport = "full-support"
	""" Conditional reads are supported, with both If-Modified-Since and If-None-Match HTTP Headers.
	"""
}


class ConformanceExpectation(object) {
	""" Indicates the degree of adherence to a specified behavior or capability expected for a system to be deemed conformant
with a specification.

	URL: http://terminology.hl7.org/CodeSystem/conformance-expectation
	ValueSet: http://hl7.org/fhir/ValueSet/conformance-expectation
	"""
	
	SHALL = "SHALL"
	""" Support for the specified capability is required to be considered conformant.
	"""
	
	SHOULD = "SHOULD"
	""" Support for the specified capability is strongly encouraged, and failure to support it should only occur after
	/// careful consideration.
	"""
	
	MAY = "MAY"
	""" Support for the specified capability is not necessary to be considered conformant, and the requirement should be
	/// considered strictly optional.
	"""
	
	SHOULDNOT = "SHOULD-NOT"
	""" Support for the specified capability is strongly discouraged and should occur only after careful consideration.
	"""
}


class ConsentDataMeaning(object) {
	""" How a resource reference is interpreted when testing consent restrictions.

	URL: http://hl7.org/fhir/consent-data-meaning
	ValueSet: http://hl7.org/fhir/ValueSet/consent-data-meaning
	"""
	
	instance = "instance"
	""" The consent applies directly to the instance of the resource.
	"""
	
	related = "related"
	""" The consent applies directly to the instance of the resource and instances it refers to.
	"""
	
	dependents = "dependents"
	""" The consent applies directly to the instance of the resource and instances that refer to it.
	"""
	
	authoredby = "authoredby"
	""" The consent applies to instances of resources that are authored by.
	"""
}


class ConsentProvisionType(object) {
	""" How a rule statement is applied, such as adding additional consent or removing consent.

	URL: http://hl7.org/fhir/consent-provision-type
	ValueSet: http://hl7.org/fhir/ValueSet/consent-provision-type
	"""
	
	deny = "deny"
	""" Consent is denied for actions meeting these rules.
	"""
	
	permit = "permit"
	""" Consent is provided for actions meeting these rules.
	"""
}


class ConstraintSeverity(object) {
	""" SHALL applications comply with this constraint?

	URL: http://hl7.org/fhir/constraint-severity
	ValueSet: http://hl7.org/fhir/ValueSet/constraint-severity
	"""
	
	error = "error"
	""" If the constraint is violated, the resource is not conformant.
	"""
	
	warning = "warning"
	""" If the constraint is violated, the resource is conformant, but it is not necessarily following best practice.
	"""
}


class ContactPointSystem(object) {
	""" Telecommunications form for contact point.

	URL: http://hl7.org/fhir/contact-point-system
	ValueSet: http://hl7.org/fhir/ValueSet/contact-point-system
	"""
	
	phone = "phone"
	""" The value is a telephone number used for voice calls. Use of full international numbers starting with + is
	/// recommended to enable automatic dialing support but not required.
	"""
	
	fax = "fax"
	""" The value is a fax machine. Use of full international numbers starting with + is recommended to enable automatic
	/// dialing support but not required.
	"""
	
	email = "email"
	""" The value is an email address.
	"""
	
	pager = "pager"
	""" The value is a pager number. These may be local pager numbers that are only usable on a particular pager system.
	"""
	
	url = "url"
	""" A contact that is not a phone, fax, pager or email address and is expressed as a URL.  This is intended for
	/// various institutional or personal contacts including web sites, blogs, Skype, Twitter, Facebook, etc. Do not use
	/// for email addresses.
	"""
	
	sms = "sms"
	""" A contact that can be used for sending an sms message (e.g. mobile phones, some landlines).
	"""
	
	other = "other"
	""" A contact that is not a phone, fax, page or email address and is not expressible as a URL.  E.g. Internal mail
	/// address.  This SHOULD NOT be used for contacts that are expressible as a URL (e.g. Skype, Twitter, Facebook,
	/// etc.)  Extensions may be used to distinguish "other" contact types.
	"""
}


class ContactPointUse(object) {
	""" Use of contact point.

	URL: http://hl7.org/fhir/contact-point-use
	ValueSet: http://hl7.org/fhir/ValueSet/contact-point-use
	"""
	
	home = "home"
	""" A communication contact point at a home; attempted contacts for business purposes might intrude privacy and
	/// chances are one will contact family or other household members instead of the person one wishes to call.
	/// Typically used with urgent cases, or if no other contacts are available.
	"""
	
	work = "work"
	""" An office contact point. First choice for business related contacts during business hours.
	"""
	
	temp = "temp"
	""" A temporary contact point. The period can provide more detailed information.
	"""
	
	old = "old"
	""" This contact point is no longer in use (or was never correct, but retained for records).
	"""
	
	mobile = "mobile"
	""" A telecommunication device that moves and stays with its owner. May have characteristics of all other use codes,
	/// suitable for urgent matters, not the first choice for routine business.
	"""
}


class ContainerCap(object) {
	""" Color of the container cap.

	URL: http://terminology.hl7.org/CodeSystem/container-cap
	ValueSet: http://hl7.org/fhir/ValueSet/container-cap
	"""
	
	red = "red"
	""" red cap.
	"""
	
	yellow = "yellow"
	""" yellow cap.
	"""
	
	grey = "grey"
	""" grey cap.
	"""
	
	violet = "violet"
	""" violet cap.
	"""
	
	blue = "blue"
	""" blue cap.
	"""
	
	black = "black"
	""" black cap.
	"""
	
	green = "green"
	""" green cap.
	"""
}


class ContractDataMeaning(object) {
	""" How a resource reference is interpreted when evaluating contract offers.

	URL: http://terminology.hl7.org/CodeSystem/contract-data-meaning
	ValueSet: http://hl7.org/fhir/ValueSet/contract-data-meaning
	"""
	
	instance = "instance"
	""" The consent applies directly to the instance of the resource.
	"""
	
	related = "related"
	""" The consent applies directly to the instance of the resource and instances it refers to.
	"""
	
	dependents = "dependents"
	""" The consent applies directly to the instance of the resource and instances that refer to it.
	"""
	
	authoredby = "authoredby"
	""" The consent applies to instances of resources that are authored by.
	"""
}


class ContributorType(object) {
	""" The type of contributor.

	URL: http://hl7.org/fhir/contributor-type
	ValueSet: http://hl7.org/fhir/ValueSet/contributor-type
	"""
	
	author = "author"
	""" An author of the content of the module.
	"""
	
	editor = "editor"
	""" An editor of the content of the module.
	"""
	
	reviewer = "reviewer"
	""" A reviewer of the content of the module.
	"""
	
	endorser = "endorser"
	""" An endorser of the content of the module.
	"""
}


class CopyNumberEvent(object) {
	""" Copy Number Event.

	URL: http://terminology.hl7.org/CodeSystem/copy-number-event
	ValueSet: http://hl7.org/fhir/ValueSet/copy-number-event
	"""
	
	amp = "amp"
	""" amplification.
	"""
	
	del = "del"
	""" deletion.
	"""
	
	lof = "lof"
	""" loss of function.
	"""
}


class DataAbsentReason(object) {
	""" Used to specify why the normally expected content of the data element is missing.

	URL: http://terminology.hl7.org/CodeSystem/data-absent-reason
	ValueSet: http://hl7.org/fhir/ValueSet/data-absent-reason
	"""
	
	unknown = "unknown"
	""" The value is expected to exist but is not known.
	"""
	
	askedUnknown = "asked-unknown"
	""" The source was asked but does not know the value.
	"""
	
	tempUnknown = "temp-unknown"
	""" There is reason to expect (from the workflow) that the value may become known.
	"""
	
	notAsked = "not-asked"
	""" The workflow didn't lead to this value being known.
	"""
	
	askedDeclined = "asked-declined"
	""" The source was asked but declined to answer.
	"""
	
	masked = "masked"
	""" The information is not available due to security, privacy or related reasons.
	"""
	
	notApplicable = "not-applicable"
	""" There is no proper value for this element (e.g. last menstrual period for a male).
	"""
	
	unsupported = "unsupported"
	""" The source system wasn't capable of supporting this element.
	"""
	
	asText = "as-text"
	""" The content of the data is represented in the resource narrative.
	"""
	
	error = "error"
	""" Some system or workflow process error means that the information is not available.
	"""
	
	notANumber = "not-a-number"
	""" The numeric value is undefined or unrepresentable due to a floating point processing error.
	"""
	
	negativeInfinity = "negative-infinity"
	""" The numeric value is excessively low and unrepresentable due to a floating point processing error.
	"""
	
	positiveInfinity = "positive-infinity"
	""" The numeric value is excessively high and unrepresentable due to a floating point processing error.
	"""
	
	notPerformed = "not-performed"
	""" The value is not available because the observation procedure (test, etc.) was not performed.
	"""
	
	notPermitted = "not-permitted"
	""" The value is not permitted in this context (e.g. due to profiles, or the base data types).
	"""
}


class DataType(object) {
	""" A version specific list of the data types defined by the FHIR specification for use as an element  type (any of the FHIR
defined data types).

	URL: http://hl7.org/fhir/data-types
	"""
	
	address = "Address"
	""" An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This
	/// data type may be used to convey addresses for use in delivering mail as well as for visiting locations which
	/// might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
	"""
	
	age = "Age"
	""" A duration of time during which an organism (or a process) has existed.
	"""
	
	annotation = "Annotation"
	""" A  text note which also  contains information about who made the statement and when.
	"""
	
	attachment = "Attachment"
	""" For referring to data content defined in other formats.
	"""
	
	backboneElement = "BackboneElement"
	""" Base definition for all elements that are defined inside a resource - but not those in a data type.
	"""
	
	codeableConcept = "CodeableConcept"
	""" A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
	"""
	
	coding = "Coding"
	""" A reference to a code defined by a terminology system.
	"""
	
	contactDetail = "ContactDetail"
	""" Specifies contact information for a person or organization.
	"""
	
	contactPoint = "ContactPoint"
	""" Details for all kinds of technology mediated contact points for a person or organization, including telephone,
	/// email, etc.
	"""
	
	contributor = "Contributor"
	""" A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
	"""
	
	count = "Count"
	""" A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts
	/// that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
	"""
	
	dataRequirement = "DataRequirement"
	""" Describes a required data item for evaluation in terms of the type of data, and optional code or date-based
	/// filters of the data.
	"""
	
	distance = "Distance"
	""" A length - a value with a unit that is a physical distance.
	"""
	
	dosage = "Dosage"
	""" Indicates how the medication is/was taken or should be taken by the patient.
	"""
	
	duration = "Duration"
	""" A length of time.
	"""
	
	element = "Element"
	""" Base definition for all elements in a resource.
	"""
	
	elementDefinition = "ElementDefinition"
	""" Captures constraints on each element within the resource, profile, or extension.
	"""
	
	expression = "Expression"
	""" A expression that is evaluated in a specified context and returns a value. The context of use of the expression
	/// must specify the context in which the expression is evaluated, and how the result of the expression is used.
	"""
	
	extension = "Extension"
	""" Optional Extension Element - found in all resources.
	"""
	
	humanName = "HumanName"
	""" A human's name with the ability to identify parts and usage.
	"""
	
	identifier = "Identifier"
	""" An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business
	/// identifiers.
	"""
	
	marketingStatus = "MarketingStatus"
	""" The marketing status describes the date when a medicinal product is actually put on the market or the date as of
	/// which it is no longer available.
	"""
	
	meta = "Meta"
	""" The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes
	/// to the content might not always be associated with version changes to the resource.
	"""
	
	money = "Money"
	""" An amount of economic utility in some recognized currency.
	"""
	
	moneyQuantity = "MoneyQuantity"
	""" moneyQuantity
	"""
	
	narrative = "Narrative"
	""" A human-readable summary of the resource conveying the essential clinical and business information for the
	/// resource.
	"""
	
	parameterDefinition = "ParameterDefinition"
	""" The parameters to the module. This collection specifies both the input and output parameters. Input parameters
	/// are provided by the caller as part of the $evaluate operation. Output parameters are included in the
	/// GuidanceResponse.
	"""
	
	period = "Period"
	""" A time period defined by a start and end date and optionally time.
	"""
	
	population = "Population"
	""" A populatioof people with some set of grouping criteria.
	"""
	
	prodCharacteristic = "ProdCharacteristic"
	""" The marketing status describes the date when a medicinal product is actually put on the market or the date as of
	/// which it is no longer available.
	"""
	
	productShelfLife = "ProductShelfLife"
	""" The shelf-life and storage information for a medicinal product item or container can be described using this
	/// class.
	"""
	
	quantity = "Quantity"
	""" A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts
	/// that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
	"""
	
	range = "Range"
	""" A set of ordered Quantities defined by a low and high limit.
	"""
	
	ratio = "Ratio"
	""" A relationship of two Quantity values - expressed as a numerator and a denominator.
	"""
	
	reference = "Reference"
	""" A reference from one resource to another.
	"""
	
	relatedArtifact = "RelatedArtifact"
	""" Related artifacts such as additional documentation, justification, or bibliographic references.
	"""
	
	sampledData = "SampledData"
	""" A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in
	/// the data.
	"""
	
	signature = "Signature"
	""" A signature along with supporting context. The signature may be a digital signature that is cryptographic in
	/// nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical
	/// image representing a hand-written signature, or a signature ceremony Different signature approaches have
	/// different utilities.
	"""
	
	simpleQuantity = "SimpleQuantity"
	""" simpleQuantity
	"""
	
	substanceAmount = "SubstanceAmount"
	""" Chemical substances are a single substance type whose primary defining element is the molecular structure.
	/// Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence
	/// of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or
	/// particle size are not taken into account in the definition of a chemical substance or in the assignment of a
	/// Substance ID.
	"""
	
	timing = "Timing"
	""" Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned,
	/// expected or requested to occur. The most common usage is in dosage instructions for medications. They are also
	/// used when planning care of various kinds, and may be used for reporting the schedule to which past regular
	/// activities were carried out.
	"""
	
	triggerDefinition = "TriggerDefinition"
	""" A description of a triggering event. Triggering events can be named events, data events, or periodic, as
	/// determined by the type element.
	"""
	
	usageContext = "UsageContext"
	""" Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact.
	/// This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific
	/// context of care (e.g., venue, care setting, provider of care).
	"""
	
	base64Binary = "base64Binary"
	""" A stream of bytes
	"""
	
	boolean = "boolean"
	""" Value of "true" or "false"
	"""
	
	canonical = "canonical"
	""" A URI that is a reference to a canonical URL on a FHIR resource
	"""
	
	code = "code"
	""" A string which has at least one character and no leading or trailing whitespace and where there is no whitespace
	/// other than single spaces in the contents
	"""
	
	date = "date"
	""" A date or partial date (e.g. just year or year + month). There is no time zone. The format is a union of the
	/// schema types gYear, gYearMonth and date.  Dates SHALL be valid dates.
	"""
	
	dateTime = "dateTime"
	""" A date, date-time or partial date (e.g. just year or year + month).  If hours and minutes are specified, a time
	/// zone SHALL be populated. The format is a union of the schema types gYear, gYearMonth, date and dateTime. Seconds
	/// must be provided due to schema type constraints but may be zero-filled and may be ignored.                 Dates
	/// SHALL be valid dates.
	"""
	
	decimal = "decimal"
	""" A rational number with implicit precision
	"""
	
	id = "id"
	""" Any combination of letters, numerals, "-" and ".", with a length limit of 64 characters.  (This might be an
	/// integer, an unprefixed OID, UUID or any other identifier pattern that meets these constraints.)  Ids are case-
	/// insensitive.
	"""
	
	instant = "instant"
	""" An instant in time - known at least to the second
	"""
	
	integer = "integer"
	""" A whole number
	"""
	
	markdown = "markdown"
	""" A string that may contain Github Flavored Markdown syntax for optional processing by a mark down presentation
	/// engine
	"""
	
	oid = "oid"
	""" An OID represented as a URI
	"""
	
	positiveInt = "positiveInt"
	""" An integer with a value that is positive (e.g. >0)
	"""
	
	string = "string"
	""" A sequence of Unicode characters
	"""
	
	time = "time"
	""" A time during the day, with no date specified
	"""
	
	unsignedInt = "unsignedInt"
	""" An integer with a value that is not negative (e.g. >= 0)
	"""
	
	uri = "uri"
	""" String of characters used to identify a name or a resource
	"""
	
	url = "url"
	""" A URI that is a literal reference
	"""
	
	uuid = "uuid"
	""" A UUID, represented as a URI
	"""
	
	xhtml = "xhtml"
	""" XHTML format, as defined by W3C, but restricted usage (mainly, no active content)
	"""
}


class DaysOfWeek(object) {
	""" The days of the week.

	URL: http://hl7.org/fhir/days-of-week
	ValueSet: http://hl7.org/fhir/ValueSet/days-of-week
	"""
	
	mon = "mon"
	""" Monday.
	"""
	
	tue = "tue"
	""" Tuesday.
	"""
	
	wed = "wed"
	""" Wednesday.
	"""
	
	thu = "thu"
	""" Thursday.
	"""
	
	fri = "fri"
	""" Friday.
	"""
	
	sat = "sat"
	""" Saturday.
	"""
	
	sun = "sun"
	""" Sunday.
	"""
}


class DefinitionResourceType(object) {
	""" A list of all the definition resource types defined in this version of the FHIR specification.

	URL: http://hl7.org/fhir/definition-resource-types
	ValueSet: http://hl7.org/fhir/ValueSet/definition-resource-types
	"""
	
	activityDefinition = "ActivityDefinition"
	""" This resource allows for the definition of some activity to be performed, independent of a particular patient,
	/// practitioner, or other performance context.
	"""
	
	eventDefinition = "EventDefinition"
	""" The EventDefinition resource provides a reusable description of when a particular event can occur.
	"""
	
	measure = "Measure"
	""" The Measure resource provides the definition of a quality measure.
	"""
	
	operationDefinition = "OperationDefinition"
	""" A formal computable definition of an operation (on the RESTful interface) or a named query (using the search
	/// interaction).
	"""
	
	planDefinition = "PlanDefinition"
	""" This resource allows for the definition of various types of plans as a sharable, consumable, and executable
	/// artifact. The resource is general enough to support the description of a broad range of clinical artifacts such
	/// as clinical decision support rules, order sets and protocols.
	"""
	
	questionnaire = "Questionnaire"
	""" A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide
	/// detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data
	/// collection.
	"""
}


class DefinitionStatus(object) {
	""" Codes identifying the lifecycle stage of a definition.

	URL: http://terminology.hl7.org/CodeSystem/definition-status
	ValueSet: http://hl7.org/fhir/ValueSet/definition-status
	"""
	
	draft = "draft"
	""" The definition is in the design stage and is not yet considered to be "ready for use".
	"""
	
	active = "active"
	""" The definition is considered ready for use.
	"""
	
	withdrawn = "withdrawn"
	""" The definition should no longer be used.
	"""
	
	unknown = "unknown"
	""" The authoring system does not know which of the status values currently applies for this request.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
	"""
}


class DefinitionTopic(object) {
	""" High-level categorization of the definition, used for searching, sorting, and filtering.

	URL: http://terminology.hl7.org/CodeSystem/definition-topic
	ValueSet: http://hl7.org/fhir/ValueSet/definition-topic
	"""
	
	treatment = "treatment"
	""" The definition is related to treatment of the patient.
	"""
	
	education = "education"
	""" The definition is related to education of the patient.
	"""
	
	assessment = "assessment"
	""" The definition is related to assessment of the patient.
	"""
}


class DetectedIssueSeverity(object) {
	""" Indicates the potential degree of impact of the identified issue on the patient.

	URL: http://hl7.org/fhir/detectedissue-severity
	ValueSet: http://hl7.org/fhir/ValueSet/detectedissue-severity
	"""
	
	high = "high"
	""" Indicates the issue may be life-threatening or has the potential to cause permanent injury.
	"""
	
	moderate = "moderate"
	""" Indicates the issue may result in noticeable adverse consequences but is unlikely to be life-threatening or
	/// cause permanent injury.
	"""
	
	low = "low"
	""" Indicates the issue may result in some adverse consequences but is unlikely to substantially affect the
	/// situation of the subject.
	"""
}


class DeviceDefinitionParameterGroup(object) {
	""" Codes identifying groupings of parameters; e.g. Cardiovascular.

	URL: http://terminology.hl7.org/CodeSystem/parameter-group
	ValueSet: http://hl7.org/fhir/ValueSet/parameter-group
	"""
	
	haemodynamic = "haemodynamic"
	""" Haemodynamic Parameter Group - MDC_PGRP_HEMO.
	"""
	
	ecg = "ecg"
	""" ECG Parameter Group - MDC_PGRP_ECG.
	"""
	
	respiratory = "respiratory"
	""" Respiratory Parameter Group - MDC_PGRP_RESP.
	"""
	
	ventilation = "ventilation"
	""" Ventilation Parameter Group - MDC_PGRP_VENT.
	"""
	
	neurological = "neurological"
	""" Neurological Parameter Group - MDC_PGRP_NEURO.
	"""
	
	drugDelivery = "drug-delivery"
	""" Drug Delivery Parameter Group - MDC_PGRP_DRUG.
	"""
	
	fluidChemistry = "fluid-chemistry"
	""" Fluid Chemistry Parameter Group - MDC_PGRP_FLUID.
	"""
	
	bloodChemistry = "blood-chemistry"
	""" Blood Chemistry Parameter Group - MDC_PGRP_BLOOD_CHEM.
	"""
	
	miscellaneous = "miscellaneous"
	""" Miscellaneous Parameter Group - MDC_PGRP_MISC.
	"""
}


class DeviceMetricCalibrationState(object) {
	""" Describes the state of a metric calibration.

	URL: http://hl7.org/fhir/metric-calibration-state
	ValueSet: http://hl7.org/fhir/ValueSet/metric-calibration-state
	"""
	
	notCalibrated = "not-calibrated"
	""" The metric has not been calibrated.
	"""
	
	calibrationRequired = "calibration-required"
	""" The metric needs to be calibrated.
	"""
	
	calibrated = "calibrated"
	""" The metric has been calibrated.
	"""
	
	unspecified = "unspecified"
	""" The state of calibration of this metric is unspecified.
	"""
}


class DeviceMetricCalibrationType(object) {
	""" Describes the type of a metric calibration.

	URL: http://hl7.org/fhir/metric-calibration-type
	ValueSet: http://hl7.org/fhir/ValueSet/metric-calibration-type
	"""
	
	unspecified = "unspecified"
	""" Metric calibration method has not been identified.
	"""
	
	offset = "offset"
	""" Offset metric calibration method.
	"""
	
	gain = "gain"
	""" Gain metric calibration method.
	"""
	
	twoPoint = "two-point"
	""" Two-point metric calibration method.
	"""
}


class DeviceMetricCategory(object) {
	""" Describes the category of the metric.

	URL: http://hl7.org/fhir/metric-category
	ValueSet: http://hl7.org/fhir/ValueSet/metric-category
	"""
	
	measurement = "measurement"
	""" DeviceObservations generated for this DeviceMetric are measured.
	"""
	
	setting = "setting"
	""" DeviceObservations generated for this DeviceMetric is a setting that will influence the behavior of the Device.
	"""
	
	calculation = "calculation"
	""" DeviceObservations generated for this DeviceMetric are calculated.
	"""
	
	unspecified = "unspecified"
	""" The category of this DeviceMetric is unspecified.
	"""
}


class DeviceMetricColor(object) {
	""" Describes the typical color of representation.

	URL: http://hl7.org/fhir/metric-color
	ValueSet: http://hl7.org/fhir/ValueSet/metric-color
	"""
	
	black = "black"
	""" Color for representation - black.
	"""
	
	red = "red"
	""" Color for representation - red.
	"""
	
	green = "green"
	""" Color for representation - green.
	"""
	
	yellow = "yellow"
	""" Color for representation - yellow.
	"""
	
	blue = "blue"
	""" Color for representation - blue.
	"""
	
	magenta = "magenta"
	""" Color for representation - magenta.
	"""
	
	cyan = "cyan"
	""" Color for representation - cyan.
	"""
	
	white = "white"
	""" Color for representation - white.
	"""
}


class DeviceMetricOperationalStatus(object) {
	""" Describes the operational status of the DeviceMetric.

	URL: http://hl7.org/fhir/metric-operational-status
	ValueSet: http://hl7.org/fhir/ValueSet/metric-operational-status
	"""
	
	on = "on"
	""" The DeviceMetric is operating and will generate DeviceObservations.
	"""
	
	off = "off"
	""" The DeviceMetric is not operating.
	"""
	
	standby = "standby"
	""" The DeviceMetric is operating, but will not generate any DeviceObservations.
	"""
	
	enteredInError = "entered-in-error"
	""" The DeviceMetric was entered in error.
	"""
}


class DeviceNameType(object) {
	""" The type of name the device is referred by.

	URL: http://hl7.org/fhir/device-nametype
	ValueSet: http://hl7.org/fhir/ValueSet/device-nametype
	"""
	
	udiLabelName = "udi-label-name"
	""" UDI Label name.
	"""
	
	userFriendlyName = "user-friendly-name"
	""" User Friendly name.
	"""
	
	patientReportedName = "patient-reported-name"
	""" Patient Reported name.
	"""
	
	manufacturerName = "manufacturer-name"
	""" Manufacturer name.
	"""
	
	modelName = "model-name"
	""" Model name.
	"""
	
	other = "other"
	""" other.
	"""
}


class DeviceUseStatementStatus(object) {
	""" A coded concept indicating the current status of the Device Usage.

	URL: http://hl7.org/fhir/device-statement-status
	ValueSet: http://hl7.org/fhir/ValueSet/device-statement-status
	"""
	
	active = "active"
	""" The device is still being used.
	"""
	
	completed = "completed"
	""" The device is no longer being used.
	"""
	
	enteredInError = "entered-in-error"
	""" The statement was recorded incorrectly.
	"""
	
	intended = "intended"
	""" The device may be used at some time in the future.
	"""
	
	stopped = "stopped"
	""" Actions implied by the statement have been permanently halted, before all of them occurred.
	"""
	
	onHold = "on-hold"
	""" Actions implied by the statement have been temporarily halted, but are expected to continue later. May also be
	/// called "suspended".
	"""
}


class DiagnosticReportStatus(object) {
	""" The status of the diagnostic report.

	URL: http://hl7.org/fhir/diagnostic-report-status
	ValueSet: http://hl7.org/fhir/ValueSet/diagnostic-report-status
	"""
	
	registered = "registered"
	""" The existence of the report is registered, but there is nothing yet available.
	"""
	
	partial = "partial"
	""" This is a partial (e.g. initial, interim or preliminary) report: data in the report may be incomplete or
	/// unverified.
	"""
	
	preliminary = "preliminary"
	""" Verified early results are available, but not all  results are final.
	"""
	
	final = "final"
	""" The report is complete and verified by an authorized person.
	"""
	
	amended = "amended"
	""" Subsequent to being final, the report has been modified.  This includes any change in the results, diagnosis,
	/// narrative text, or other content of a report that has been issued.
	"""
	
	corrected = "corrected"
	""" Subsequent to being final, the report has been modified  to correct an error in the report or referenced
	/// results.
	"""
	
	appended = "appended"
	""" Subsequent to being final, the report has been modified by adding new content. The existing content is
	/// unchanged.
	"""
	
	cancelled = "cancelled"
	""" The report is unavailable because the measurement was not started or not completed (also sometimes called
	/// "aborted").
	"""
	
	enteredInError = "entered-in-error"
	""" The report has been withdrawn following a previous final release.  This electronic record should never have
	/// existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred,
	/// the status should be "cancelled" rather than "entered-in-error".).
	"""
	
	unknown = "unknown"
	""" The authoring/source system does not know which of the status values currently applies for this observation.
	/// Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the
	/// authoring/source system does not know which.
	"""
}


class DiscriminatorType(object) {
	""" How an element value is interpreted when discrimination is evaluated.

	URL: http://hl7.org/fhir/discriminator-type
	ValueSet: http://hl7.org/fhir/ValueSet/discriminator-type
	"""
	
	value = "value"
	""" The slices have different values in the nominated element.
	"""
	
	exists = "exists"
	""" The slices are differentiated by the presence or absence of the nominated element.
	"""
	
	pattern = "pattern"
	""" The slices have different values in the nominated element, as determined by testing them against the applicable
	/// ElementDefinition.pattern[x].
	"""
	
	type = "type"
	""" The slices are differentiated by type of the nominated element.
	"""
	
	profile = "profile"
	""" The slices are differentiated by conformance of the nominated element to a specified profile. Note that if the
	/// path specifies .resolve() then the profile is the target profile on the reference. In this case, validation by
	/// the possible profiles is required to differentiate the slices.
	"""
}


class DocumentMode(object) {
	""" Whether the application produces or consumes documents.

	URL: http://hl7.org/fhir/document-mode
	ValueSet: http://hl7.org/fhir/ValueSet/document-mode
	"""
	
	producer = "producer"
	""" The application produces documents of the specified type.
	"""
	
	consumer = "consumer"
	""" The application consumes documents of the specified type.
	"""
}


class DocumentReferenceStatus(object) {
	""" The status of the document reference.

	URL: http://hl7.org/fhir/document-reference-status
	ValueSet: http://hl7.org/fhir/ValueSet/document-reference-status
	"""
	
	current = "current"
	""" This is the current reference for this document.
	"""
	
	superseded = "superseded"
	""" This reference has been superseded by another reference.
	"""
	
	enteredInError = "entered-in-error"
	""" This reference was created in error.
	"""
}


class DocumentRelationshipType(object) {
	""" The type of relationship between documents.

	URL: http://hl7.org/fhir/document-relationship-type
	ValueSet: http://hl7.org/fhir/ValueSet/document-relationship-type
	"""
	
	replaces = "replaces"
	""" This document logically replaces or supersedes the target document.
	"""
	
	transforms = "transforms"
	""" This document was generated by transforming the target document (e.g. format or language conversion).
	"""
	
	signs = "signs"
	""" This document is a signature of the target document.
	"""
	
	appends = "appends"
	""" This document adds additional information to the target document.
	"""
}


class DoseAndRateType(object) {
	""" The kind of dose or rate specified.

	URL: http://terminology.hl7.org/CodeSystem/dose-rate-type
	ValueSet: http://hl7.org/fhir/ValueSet/dose-rate-type
	"""
	
	calculated = "calculated"
	""" The dose specified is calculated by the prescriber or the system.
	"""
	
	ordered = "ordered"
	""" The dose specified is as ordered by the prescriber.
	"""
}


class EffectEstimateType(object) {
	""" Whether the effect estimate is an absolute effect estimate (absolute difference) or a relative effect estimate (relative
difference), and the specific type of effect estimate (eg relative risk or median difference).

	URL: http://terminology.hl7.org/CodeSystem/effect-estimate-type
	ValueSet: http://hl7.org/fhir/ValueSet/effect-estimate-type
	"""
	
	relativeRR = "relative-RR"
	""" relative risk (a type of relative effect estimate).
	"""
	
	relativeOR = "relative-OR"
	""" odds ratio (a type of relative effect estimate).
	"""
	
	relativeHR = "relative-HR"
	""" hazard ratio (a type of relative effect estimate).
	"""
	
	absoluteARD = "absolute-ARD"
	""" absolute risk difference (a type of absolute effect estimate).
	"""
	
	absoluteMeanDiff = "absolute-MeanDiff"
	""" mean difference (a type of absolute effect estimate).
	"""
	
	absoluteSMD = "absolute-SMD"
	""" standardized mean difference (a type of absolute effect estimate).
	"""
	
	absoluteMedianDiff = "absolute-MedianDiff"
	""" median difference (a type of absolute effect estimate).
	"""
}


class EligibilityRequestPurpose(object) {
	""" A code specifying the types of information being requested.

	URL: http://hl7.org/fhir/eligibilityrequest-purpose
	ValueSet: http://hl7.org/fhir/ValueSet/eligibilityrequest-purpose
	"""
	
	authRequirements = "auth-requirements"
	""" The prior authorization requirements for the listed, or discovered if specified, converages for the categories
	/// of service and/or specifed biling codes are requested.
	"""
	
	benefits = "benefits"
	""" The plan benefits and optionally benefits consumed  for the listed, or discovered if specified, converages are
	/// requested.
	"""
	
	discovery = "discovery"
	""" The insurer is requested to report on any coverages which they are aware of in addition to any specifed.
	"""
	
	validation = "validation"
	""" A check that the specified coverages are in-force is requested.
	"""
}


class EligibilityResponsePurpose(object) {
	""" A code specifying the types of information being requested.

	URL: http://hl7.org/fhir/eligibilityresponse-purpose
	ValueSet: http://hl7.org/fhir/ValueSet/eligibilityresponse-purpose
	"""
	
	authRequirements = "auth-requirements"
	""" The prior authorization requirements for the listed, or discovered if specified, converages for the categories
	/// of service and/or specifed biling codes are requested.
	"""
	
	benefits = "benefits"
	""" The plan benefits and optionally benefits consumed  for the listed, or discovered if specified, converages are
	/// requested.
	"""
	
	discovery = "discovery"
	""" The insurer is requested to report on any coverages which they are aware of in addition to any specifed.
	"""
	
	validation = "validation"
	""" A check that the specified coverages are in-force is requested.
	"""
}


class EnableWhenBehavior(object) {
	""" Controls how multiple enableWhen values are interpreted -  whether all or any must be true.

	URL: http://hl7.org/fhir/questionnaire-enable-behavior
	ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-enable-behavior
	"""
	
	all = "all"
	""" Enable the question when all the enableWhen criteria are satisfied.
	"""
	
	any = "any"
	""" Enable the question when any of the enableWhen criteria are satisfied.
	"""
}


class EncounterLocationStatus(object) {
	""" The status of the location.

	URL: http://hl7.org/fhir/encounter-location-status
	ValueSet: http://hl7.org/fhir/ValueSet/encounter-location-status
	"""
	
	planned = "planned"
	""" The patient is planned to be moved to this location at some point in the future.
	"""
	
	active = "active"
	""" The patient is currently at this location, or was between the period specified.
	/// 
	/// A system may update these records when the patient leaves the location to either reserved, or completed.
	"""
	
	reserved = "reserved"
	""" This location is held empty for this patient.
	"""
	
	completed = "completed"
	""" The patient was at this location during the period specified.
	/// 
	/// Not to be used when the patient is currently at the location.
	"""
}


class EncounterStatus(object) {
	""" Current state of the encounter.

	URL: http://hl7.org/fhir/encounter-status
	ValueSet: http://hl7.org/fhir/ValueSet/encounter-status
	"""
	
	planned = "planned"
	""" The Encounter has not yet started.
	"""
	
	arrived = "arrived"
	""" The Patient is present for the encounter, however is not currently meeting with a practitioner.
	"""
	
	triaged = "triaged"
	""" The patient has been assessed for the priority of their treatment based on the severity of their condition.
	"""
	
	inProgress = "in-progress"
	""" The Encounter has begun and the patient is present / the practitioner and the patient are meeting.
	"""
	
	onleave = "onleave"
	""" The Encounter has begun, but the patient is temporarily on leave.
	"""
	
	finished = "finished"
	""" The Encounter has ended.
	"""
	
	cancelled = "cancelled"
	""" The Encounter has ended before it has begun.
	"""
	
	enteredInError = "entered-in-error"
	""" This instance should not have been part of this patient's medical record.
	"""
	
	unknown = "unknown"
	""" The encounter status is unknown. Note that "unknown" is a value of last resort and every attempt should be made
	/// to provide a meaningful value other than "unknown".
	"""
}


class EndpointStatus(object) {
	""" The status of the endpoint.

	URL: http://hl7.org/fhir/endpoint-status
	ValueSet: http://hl7.org/fhir/ValueSet/endpoint-status
	"""
	
	active = "active"
	""" This endpoint is expected to be active and can be used.
	"""
	
	suspended = "suspended"
	""" This endpoint is temporarily unavailable.
	"""
	
	error = "error"
	""" This endpoint has exceeded connectivity thresholds and is considered in an error state and should no longer be
	/// attempted to connect to until corrective action is taken.
	"""
	
	off = "off"
	""" This endpoint is no longer to be used.
	"""
	
	enteredInError = "entered-in-error"
	""" This instance should not have been part of this patient's medical record.
	"""
	
	test = "test"
	""" This endpoint is not intended for production usage.
	"""
}


class EpisodeOfCareStatus(object) {
	""" The status of the episode of care.

	URL: http://hl7.org/fhir/episode-of-care-status
	ValueSet: http://hl7.org/fhir/ValueSet/episode-of-care-status
	"""
	
	planned = "planned"
	""" This episode of care is planned to start at the date specified in the period.start. During this status, an
	/// organization may perform assessments to determine if the patient is eligible to receive services, or be
	/// organizing to make resources available to provide care services.
	"""
	
	waitlist = "waitlist"
	""" This episode has been placed on a waitlist, pending the episode being made active (or cancelled).
	"""
	
	active = "active"
	""" This episode of care is current.
	"""
	
	onhold = "onhold"
	""" This episode of care is on hold, the organization has limited responsibility for the patient (such as while on
	/// respite).
	"""
	
	finished = "finished"
	""" This episode of care is finished and the organization is not expecting to be providing further care to the
	/// patient. Can also be known as "closed", "completed" or other similar terms.
	"""
	
	cancelled = "cancelled"
	""" The episode of care was cancelled, or withdrawn from service, often selected during the planned stage as the
	/// patient may have gone elsewhere, or the circumstances have changed and the organization is unable to provide the
	/// care. It indicates that services terminated outside the planned/expected workflow.
	"""
	
	enteredInError = "entered-in-error"
	""" This instance should not have been part of this patient's medical record.
	"""
}


class EventCapabilityMode(object) {
	""" The mode of a message capability statement.

	URL: http://hl7.org/fhir/event-capability-mode
	ValueSet: http://hl7.org/fhir/ValueSet/event-capability-mode
	"""
	
	sender = "sender"
	""" The application sends requests and receives responses.
	"""
	
	receiver = "receiver"
	""" The application receives requests and sends responses.
	"""
}


class EventResourceType(object) {
	""" A list of all the event resource types defined in this version of the FHIR specification.

	URL: http://hl7.org/fhir/event-resource-types
	ValueSet: http://hl7.org/fhir/ValueSet/event-resource-types
	"""
	
	chargeItem = "ChargeItem"
	""" Item containing charge code(s) associated with the provision of healthcare provider products.
	"""
	
	claimResponse = "ClaimResponse"
	""" Remittance resource.
	"""
	
	clinicalImpression = "ClinicalImpression"
	""" A clinical assessment performed when planning treatments and management strategies for a patient.
	"""
	
	communication = "Communication"
	""" A record of information transmitted from a sender to a receiver.
	"""
	
	composition = "Composition"
	""" A set of resources composed into a single coherent clinical statement with clinical attestation.
	"""
	
	condition = "Condition"
	""" Detailed information about conditions, problems or diagnoses.
	"""
	
	consent = "Consent"
	""" A healthcare consumer's policy choices to permits or denies recipients or roles to perform actions for specific
	/// purposes and periods of time.
	"""
	
	coverage = "Coverage"
	""" Insurance or medical plan or a payment agreement.
	"""
	
	deviceUseStatement = "DeviceUseStatement"
	""" Record of use of a device.
	"""
	
	diagnosticReport = "DiagnosticReport"
	""" A Diagnostic report - a combination of request information, atomic results, images, interpretation, as well as
	/// formatted reports.
	"""
	
	documentManifest = "DocumentManifest"
	""" A list that defines a set of documents.
	"""
	
	documentReference = "DocumentReference"
	""" A reference to a document.
	"""
	
	encounter = "Encounter"
	""" An interaction during which services are provided to the patient.
	"""
	
	enrollmentResponse = "EnrollmentResponse"
	""" EnrollmentResponse resource.
	"""
	
	episodeOfCare = "EpisodeOfCare"
	""" An association of a Patient with an Organization and  Healthcare Provider(s) for a period of time that the
	/// Organization assumes some level of responsibility.
	"""
	
	explanationOfBenefit = "ExplanationOfBenefit"
	""" Explanation of Benefit resource.
	"""
	
	familyMemberHistory = "FamilyMemberHistory"
	""" Information about patient's relatives, relevant for patient.
	"""
	
	guidanceResponse = "GuidanceResponse"
	""" The formal response to a guidance request.
	"""
	
	imagingStudy = "ImagingStudy"
	""" A set of images produced in single study (one or more series of references images).
	"""
	
	immunization = "Immunization"
	""" Immunization event information.
	"""
	
	measureReport = "MeasureReport"
	""" Results of a measure evaluation.
	"""
	
	media = "Media"
	""" A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided
	/// by direct reference.
	"""
	
	medicationAdministration = "MedicationAdministration"
	""" Administration of medication to a patient.
	"""
	
	medicationDispense = "MedicationDispense"
	""" Dispensing a medication to a named patient.
	"""
	
	medicationStatement = "MedicationStatement"
	""" Record of medication being taken by a patient.
	"""
	
	observation = "Observation"
	""" Measurements and simple assertions.
	"""
	
	paymentNotice = "PaymentNotice"
	""" PaymentNotice request.
	"""
	
	paymentReconciliation = "PaymentReconciliation"
	""" PaymentReconciliation resource.
	"""
	
	procedure = "Procedure"
	""" An action that is being or was performed on a patient.
	"""
	
	processResponse = "ProcessResponse"
	""" ProcessResponse resource.
	"""
	
	questionnaireResponse = "QuestionnaireResponse"
	""" A structured set of questions and their answers.
	"""
	
	riskAssessment = "RiskAssessment"
	""" Potential outcomes for a subject with likelihood.
	"""
	
	supplyDelivery = "SupplyDelivery"
	""" Delivery of bulk Supplies.
	"""
	
	task = "Task"
	""" A task to be performed.
	"""
}


class EventStatus(object) {
	""" Codes identifying the lifecycle stage of an event.

	URL: http://hl7.org/fhir/event-status
	ValueSet: http://hl7.org/fhir/ValueSet/event-status
	"""
	
	preparation = "preparation"
	""" The core event has not started yet, but some staging activities have begun (e.g. surgical suite preparation).
	/// Preparation stages may be tracked for billing purposes.
	"""
	
	inProgress = "in-progress"
	""" The event is currently occurring.
	"""
	
	notDone = "not-done"
	""" The event was terminated prior to any activity beyond preparation.  I.e. The 'main' activity has not yet begun.
	/// The boundary between preparatory and the 'main' activity is context-specific.
	"""
	
	onHold = "on-hold"
	""" The event has been temporarily stopped but is expected to resume in the future.
	"""
	
	stopped = "stopped"
	""" The event was terminated prior to the full completion of the intended activity but after at least some of the
	/// 'main' activity (beyond preparation) has occurred.
	"""
	
	completed = "completed"
	""" The event has now concluded.
	"""
	
	enteredInError = "entered-in-error"
	""" This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
	"""
	
	unknown = "unknown"
	""" The authoring system does not know which of the status values currently applies for this request.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
	"""
}


class EventTiming(object) {
	""" Real world event relating to the schedule.

	URL: http://hl7.org/fhir/event-timing
	"""
	
	MORN = "MORN"
	""" Event occurs during the morning. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
	"""
	
	mORNEarly = "MORN.early"
	""" Event occurs during the early morning. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
	"""
	
	mORNLate = "MORN.late"
	""" Event occurs during the late morning. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
	"""
	
	NOON = "NOON"
	""" Event occurs around 12:00pm. The exact time is unspecified and established by institution convention or patient
	/// interpretation.
	"""
	
	AFT = "AFT"
	""" Event occurs during the afternoon. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
	"""
	
	aFTEarly = "AFT.early"
	""" Event occurs during the early afternoon. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
	"""
	
	aFTLate = "AFT.late"
	""" Event occurs during the late afternoon. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
	"""
	
	EVE = "EVE"
	""" Event occurs during the evening. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
	"""
	
	eVEEarly = "EVE.early"
	""" Event occurs during the early evening. The exact time is unspecified and established by institution convention
	/// or patient interpretation.
	"""
	
	eVELate = "EVE.late"
	""" Event occurs during the late evening. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
	"""
	
	NIGHT = "NIGHT"
	""" Event occurs during the night. The exact time is unspecified and established by institution convention or
	/// patient interpretation.
	"""
	
	PHS = "PHS"
	""" Event occurs [offset] after subject goes to sleep. The exact time is unspecified and established by institution
	/// convention or patient interpretation.
	"""
}


class EvidenceVariableType(object) {
	""" The possible types of variables for exposures or outcomes (E.g. Dichotomous, Continuous, Descriptive).

	URL: http://hl7.org/fhir/variable-type
	ValueSet: http://hl7.org/fhir/ValueSet/variable-type
	"""
	
	dichotomous = "dichotomous"
	""" The variable is dichotomous, such as present or absent.
	"""
	
	continuous = "continuous"
	""" The variable is a continuous result such as a quantity.
	"""
	
	descriptive = "descriptive"
	""" The variable is described narratively rather than quantitatively.
	"""
}


class EvidenceVariantState(object) {
	""" Used for results by exposure in variant states such as low-risk, medium-risk and high-risk states.

	URL: http://terminology.hl7.org/CodeSystem/evidence-variant-state
	ValueSet: http://hl7.org/fhir/ValueSet/evidence-variant-state
	"""
	
	lowRisk = "low-risk"
	""" low risk estimate.
	"""
	
	mediumRisk = "medium-risk"
	""" medium risk estimate.
	"""
	
	highRisk = "high-risk"
	""" high risk estimate.
	"""
}


class ExampleScenarioActorType(object) {
	""" The type of actor - system or human.

	URL: http://hl7.org/fhir/examplescenario-actor-type
	ValueSet: http://hl7.org/fhir/ValueSet/examplescenario-actor-type
	"""
	
	person = "person"
	""" A person.
	"""
	
	entity = "entity"
	""" A system.
	"""
}


class ExpansionParameterSource(object) {
	""" Declares what the source of a parameter is.

	URL: http://terminology.hl7.org/CodeSystem/expansion-parameter-source
	ValueSet: http://hl7.org/fhir/ValueSet/expansion-parameter-source
	"""
	
	input = "input"
	""" The parameter was supplied by the client in the $expand request.
	"""
	
	server = "server"
	""" The parameter was added by the expansion engine on the server.
	"""
	
	codesystem = "codesystem"
	""" The parameter was added from one the code systems used in the $expand operation.
	"""
}


class ExpansionProcessingRule(object) {
	""" Defines how concepts are processed into the expansion when it's for UI presentation.

	URL: http://terminology.hl7.org/CodeSystem/expansion-processing-rule
	ValueSet: http://hl7.org/fhir/ValueSet/expansion-processing-rule
	"""
	
	allCodes = "all-codes"
	""" The expansion (when in UI mode) includes all codes *and* any defined groups (in extensions).
	"""
	
	ungrouped = "ungrouped"
	""" The expanion (when in UI mode) lists the groups, and then any codes that have not been included in a group.
	"""
	
	groupsOnly = "groups-only"
	""" The expansion (when in UI mode) only includes the defined groups.
	"""
}


class ExplanationOfBenefitStatus(object) {
	""" A code specifying the state of the resource instance.

	URL: http://hl7.org/fhir/explanationofbenefit-status
	ValueSet: http://hl7.org/fhir/ValueSet/explanationofbenefit-status
	"""
	
	active = "active"
	""" The resource instance is currently in-force.
	"""
	
	cancelled = "cancelled"
	""" The resource instance is withdrawn, rescinded or reversed.
	"""
	
	draft = "draft"
	""" A new resource instance the contents of which is not complete.
	"""
	
	enteredInError = "entered-in-error"
	""" The resource instance was entered in error.
	"""
}


class ExposureState(object) {
	""" Whether the results by exposure is describing the results for the primary exposure of interest (exposure) or the
alternative state (exposureAlternative).

	URL: http://hl7.org/fhir/exposure-state
	ValueSet: http://hl7.org/fhir/ValueSet/exposure-state
	"""
	
	exposure = "exposure"
	""" used when the results by exposure is describing the results for the primary exposure of interest.
	"""
	
	exposureAlternative = "exposure-alternative"
	""" used when the results by exposure is describing the results for the alternative exposure state, control state or
	/// comparator state.
	"""
}


class ExpressionLanguage(object) {
	""" The media type of the expression language.

	URL: http://hl7.org/fhir/expression-language
	ValueSet: http://hl7.org/fhir/ValueSet/expression-language
	"""
	
	textCql = "text/cql"
	""" Clinical Quality Language.
	"""
	
	textFhirpath = "text/fhirpath"
	""" FHIRPath.
	"""
	
	applicationXFhirQuery = "application/x-fhir-query"
	""" FHIR's RESTful query syntax - typically independent of base URL.
	"""
}


class ExtensionContextType(object) {
	""" How an extension context is interpreted.

	URL: http://hl7.org/fhir/extension-context-type
	ValueSet: http://hl7.org/fhir/ValueSet/extension-context-type
	"""
	
	fhirpath = "fhirpath"
	""" The context is all elements that match the FHIRPath query found in the expression.
	"""
	
	element = "element"
	""" The context is any element that has an ElementDefinition.id that matches that found in the expression. This
	/// includes ElementDefinition Ids that have slicing identifiers. The full path for the element is
	/// [url]#[elementid]. If there is no #, the Element id is one defined in the base specification.
	"""
	
	extension = "extension"
	""" The context is a particular extension from a particular StructureDefinition, and the expression is just a uri
	/// that identifies the extension.
	"""
}


class FHIRDefinedConceptProperties(object) {
	""" A set of common concept properties for use on coded systems throughout the FHIR eco-system.

	URL: http://hl7.org/fhir/concept-properties
	ValueSet: http://hl7.org/fhir/ValueSet/concept-properties
	"""
	
	inactive = "inactive"
	""" True if the concept is not considered active - e.g. not a valid concept any more. Property type is boolean,
	/// default value is false
	"""
	
	deprecated = "deprecated"
	""" The date at which a concept was deprecated. Concepts that are deprecated but not inactive can still be used, but
	/// their use is discouraged, and they should be expected to be made inactive in a future release. Property type is
	/// dateTime
	"""
	
	notSelectable = "notSelectable"
	""" The concept is not intended to be chosen by the user - only intended to be used as a selector for other
	/// concepts. Note, though, that the interpretation of this is highly contextual; all concepts are selectable in
	/// some context. Property type is boolean
	"""
	
	parent = "parent"
	""" The concept identified in this property is a parent of the concept on which it is a property. The property type
	/// will be 'code'. The meaning of 'parent' is defined by the hierarchyMeaning attribute
	"""
	
	child = "child"
	""" The concept identified in this property is a child of the concept on which it is a property. The property type
	/// will be 'code'. The meaning of 'child' is defined by the hierarchyMeaning attribute
	"""
}


class FHIRDeviceStatus(object) {
	""" Codes representing the current status of the device - on, off, suspended, etc.

	URL: http://hl7.org/fhir/device-definition-status
	ValueSet: http://hl7.org/fhir/ValueSet/device-definition-status
	"""
	
	active = "active"
	""" The device is available for use.  Note: For *implanted devices*  this means that the device is implanted in the
	/// patient.
	"""
	
	inactive = "inactive"
	""" The device is no longer available for use (e.g. lost, expired, damaged).  Note: For *implanted devices*  this
	/// means that the device has been removed from the patient.
	"""
	
	enteredInError = "entered-in-error"
	""" The device was entered in error and voided.
	"""
	
	unknown = "unknown"
	""" The status of the device has not been determined.
	"""
}


class FHIRDeviceStatus(object) {
	""" The availability status of the device.

	URL: http://hl7.org/fhir/device-status
	ValueSet: http://hl7.org/fhir/ValueSet/device-status
	"""
	
	active = "active"
	""" The device is available for use.  Note: For *implanted devices*  this means that the device is implanted in the
	/// patient.
	"""
	
	inactive = "inactive"
	""" The device is no longer available for use (e.g. lost, expired, damaged).  Note: For *implanted devices*  this
	/// means that the device has been removed from the patient.
	"""
	
	enteredInError = "entered-in-error"
	""" The device was entered in error and voided.
	"""
	
	unknown = "unknown"
	""" The status of the device has not been determined.
	"""
}


class FHIRDeviceStatusReason(object) {
	""" The availability status reason of the device.

	URL: http://terminology.hl7.org/CodeSystem/device-status-reason
	ValueSet: http://hl7.org/fhir/ValueSet/device-status-reason
	"""
	
	online = "online"
	""" The device is off.
	"""
	
	paused = "paused"
	""" The device is paused.
	"""
	
	standby = "standby"
	""" The device is ready but not actively operating.
	"""
	
	offline = "offline"
	""" The device is offline.
	"""
	
	notReady = "not-ready"
	""" The device is not ready.
	"""
	
	transducDiscon = "transduc-discon"
	""" The device transducer is diconnected.
	"""
	
	hwDiscon = "hw-discon"
	""" The device hardware is disconnected.
	"""
	
	off = "off"
	""" The device is off.
	"""
}


class FHIRRestfulInteractions(object) {
	""" The set of interactions defined by the RESTful part of the FHIR specification.

	URL: http://hl7.org/fhir/restful-interaction
	ValueSet: http://hl7.org/fhir/ValueSet/restful-interaction
	"""
	
	read = "read"
	""" Read the current state of the resource.
	"""
	
	vread = "vread"
	""" Read the state of a specific version of the resource.
	"""
	
	update = "update"
	""" Update an existing resource by its id (or create it if it is new).
	"""
	
	patch = "patch"
	""" Update an existing resource by posting a set of changes to it.
	"""
	
	delete = "delete"
	""" Delete a resource.
	"""
	
	history = "history"
	""" Retrieve the change history for a particular resource, type of resource, or the entire system.
	"""
	
	historyInstance = "history-instance"
	""" Retrieve the change history for a particular resource.
	"""
	
	historyType = "history-type"
	""" Retrieve the change history for all resources of a particular type.
	"""
	
	historySystem = "history-system"
	""" Retrieve the change history for all resources on a system.
	"""
	
	create = "create"
	""" Create a new resource with a server assigned id.
	"""
	
	search = "search"
	""" Search a resource type or all resources based on some filter criteria.
	"""
	
	searchType = "search-type"
	""" Search all resources of the specified type based on some filter criteria.
	"""
	
	searchSystem = "search-system"
	""" Search all resources based on some filter criteria.
	"""
	
	capabilities = "capabilities"
	""" Get a Capability Statement for the system.
	"""
	
	transaction = "transaction"
	""" Update, create or delete a set of resources as a single transaction.
	"""
	
	batch = "batch"
	""" perform a set of a separate interactions in a single http operation
	"""
	
	operation = "operation"
	""" Perform an operation as defined by an OperationDefinition.
	"""
}


class FHIRSubstanceStatus(object) {
	""" A code to indicate if the substance is actively used.

	URL: http://hl7.org/fhir/substance-status
	ValueSet: http://hl7.org/fhir/ValueSet/substance-status
	"""
	
	active = "active"
	""" The substance is considered for use or reference.
	"""
	
	inactive = "inactive"
	""" The substance is considered for reference, but not for use.
	"""
	
	enteredInError = "entered-in-error"
	""" The substance was entered in error.
	"""
}


class FamilyHistoryAbsentReason(object) {
	""" Codes describing the reason why a family member's history is not available.

	URL: http://terminology.hl7.org/CodeSystem/history-absent-reason
	ValueSet: http://hl7.org/fhir/ValueSet/history-absent-reason
	"""
	
	subjectUnknown = "subject-unknown"
	""" Patient does not know the subject, e.g. the biological parent of an adopted patient.
	"""
	
	withheld = "withheld"
	""" The patient withheld or refused to share the information.
	"""
	
	unableToObtain = "unable-to-obtain"
	""" Information cannot be obtained; e.g. unconscious patient.
	"""
	
	deferred = "deferred"
	""" Patient does not have the information now, but can provide the information at a later date.
	"""
}


class FamilyHistoryStatus(object) {
	""" A code that identifies the status of the family history record.

	URL: http://hl7.org/fhir/history-status
	ValueSet: http://hl7.org/fhir/ValueSet/history-status
	"""
	
	partial = "partial"
	""" Some health information is known and captured, but not complete - see notes for details.
	"""
	
	completed = "completed"
	""" All available related health information is captured as of the date (and possibly time) when the family member
	/// history was taken.
	"""
	
	enteredInError = "entered-in-error"
	""" This instance should not have been part of this patient's medical record.
	"""
	
	healthUnknown = "health-unknown"
	""" Health information for this individual is unavailable/unknown.
	"""
}


class FilterOperator(object) {
	""" The kind of operation to perform as a part of a property based filter.

	URL: http://hl7.org/fhir/filter-operator
	ValueSet: http://hl7.org/fhir/ValueSet/filter-operator
	"""
	
	eq = "="
	""" The specified property of the code equals the provided value.
	"""
	
	isA = "is-a"
	""" Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value,
	/// including the provided concept itself (include descendant codes and self).
	"""
	
	descendentOf = "descendent-of"
	""" Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value,
	/// excluding the provided concept itself i.e. include descendant codes only).
	"""
	
	isNotA = "is-not-a"
	""" The specified property of the code does not have an is-a relationship with the provided value.
	"""
	
	regex = "regex"
	""" The specified property of the code  matches the regex specified in the provided value.
	"""
	
	in = "in"
	""" The specified property of the code is in the set of codes or concepts specified in the provided value (comma
	/// separated list).
	"""
	
	notIn = "not-in"
	""" The specified property of the code is not in the set of codes or concepts specified in the provided value (comma
	/// separated list).
	"""
	
	generalizes = "generalizes"
	""" Includes all concept ids that have a transitive is-a relationship from the concept Id provided as the value,
	/// including the provided concept itself (i.e. include ancestor codes and self).
	"""
	
	exists = "exists"
	""" The specified property of the code has at least one value (if the specified value is true; if the specified
	/// value is false, then matches when the specified property of the code has no values).
	"""
}


class FlagStatus(object) {
	""" Indicates whether this flag is active and needs to be displayed to a user, or whether it is no longer needed or entered
in error.

	URL: http://hl7.org/fhir/flag-status
	ValueSet: http://hl7.org/fhir/ValueSet/flag-status
	"""
	
	active = "active"
	""" A current flag that should be displayed to a user. A system may use the category to determine which roles should
	/// view the flag.
	"""
	
	inactive = "inactive"
	""" The flag does not need to be displayed any more.
	"""
	
	enteredInError = "entered-in-error"
	""" The flag was added in error, and should no longer be displayed.
	"""
}


class GoalAcceptanceStatus(object) {
	""" Codes indicating whether the goal has been accepted by a stakeholder.

	URL: http://terminology.hl7.org/CodeSystem/goal-acceptance-status
	ValueSet: http://hl7.org/fhir/ValueSet/goal-acceptance-status
	"""
	
	agree = "agree"
	""" Stakeholder supports pursuit of the goal.
	"""
	
	disagree = "disagree"
	""" Stakeholder is not in support of the pursuit of the goal.
	"""
	
	pending = "pending"
	""" Stakeholder has not yet made a decision on whether they support the goal.
	"""
}


class GoalLifecycleStatus(object) {
	""" Indicates whether the goal has been met and is still being targeted.

	URL: http://hl7.org/fhir/goal-status
	ValueSet: http://hl7.org/fhir/ValueSet/goal-status
	"""
	
	proposed = "proposed"
	""" A goal is proposed for this patient.
	"""
	
	planned = "planned"
	""" A goal is planned for this patient.
	"""
	
	accepted = "accepted"
	""" A proposed goal was accepted or acknowledged.
	"""
	
	active = "active"
	""" The goal is being sought actively.
	"""
	
	onHold = "on-hold"
	""" The goal remains a long term objective but is no longer being actively pursued for a temporary period of time.
	"""
	
	completed = "completed"
	""" The goal is no longer being sought.
	"""
	
	cancelled = "cancelled"
	""" The goal has been abandoned.
	"""
	
	enteredInError = "entered-in-error"
	""" The goal was entered in error and voided.
	"""
	
	rejected = "rejected"
	""" A proposed goal was rejected.
	"""
}


class GoalRelationshipType(object) {
	""" Types of relationships between two goals.

	URL: http://terminology.hl7.org/CodeSystem/goal-relationship-type
	ValueSet: http://hl7.org/fhir/ValueSet/goal-relationship-type
	"""
	
	predecessor = "predecessor"
	""" Indicates that the target goal is one which must be met before striving for the current goal.
	"""
	
	successor = "successor"
	""" Indicates that the target goal is a desired objective once the current goal is met.
	"""
	
	replacement = "replacement"
	""" Indicates that this goal has been replaced by the target goal.
	"""
	
	milestone = "milestone"
	""" Indicates that the target goal is considered to be a "piece" of attaining this goal.
	"""
	
	other = "other"
	""" Indicates that the relationship is not covered by one of the pre-defined codes.  (An extension may convey more
	/// information about the meaning of the relationship.).
	"""
}


class GraphCompartmentRule(object) {
	""" How a compartment must be linked.

	URL: http://hl7.org/fhir/graph-compartment-rule
	ValueSet: http://hl7.org/fhir/ValueSet/graph-compartment-rule
	"""
	
	identical = "identical"
	""" The compartment must be identical (the same literal reference).
	"""
	
	matching = "matching"
	""" The compartment must be the same - the record must be about the same patient, but the reference may be
	/// different.
	"""
	
	different = "different"
	""" The compartment must be different.
	"""
	
	custom = "custom"
	""" The compartment rule is defined in the accompanying FHIRPath expression.
	"""
}


class GraphCompartmentUse(object) {
	""" Defines how a compartment rule is used.

	URL: http://hl7.org/fhir/graph-compartment-use
	ValueSet: http://hl7.org/fhir/ValueSet/graph-compartment-use
	"""
	
	condition = "condition"
	""" This compartment rule is a condition for whether the rule applies.
	"""
	
	requirement = "requirement"
	""" This compartment rule is enforced on any relationships that meet the conditions.
	"""
}


class GroupMeasure(object) {
	""" Possible group measure aggregates (E.g. Mean, Median).

	URL: http://hl7.org/fhir/group-measure
	ValueSet: http://hl7.org/fhir/ValueSet/group-measure
	"""
	
	mean = "mean"
	""" Aggregated using Mean of participant values.
	"""
	
	median = "median"
	""" Aggregated using Median of participant values.
	"""
	
	meanOfMean = "mean-of-mean"
	""" Aggregated using Mean of study mean values.
	"""
	
	meanOfMedian = "mean-of-median"
	""" Aggregated using Mean of study median values.
	"""
	
	medianOfMean = "median-of-mean"
	""" Aggregated using Median of study mean values.
	"""
	
	medianOfMedian = "median-of-median"
	""" Aggregated using Median of study median values.
	"""
}


class GroupType(object) {
	""" Types of resources that are part of group.

	URL: http://hl7.org/fhir/group-type
	ValueSet: http://hl7.org/fhir/ValueSet/group-type
	"""
	
	person = "person"
	""" Group contains "person" Patient resources.
	"""
	
	animal = "animal"
	""" Group contains "animal" Patient resources.
	"""
	
	practitioner = "practitioner"
	""" Group contains healthcare practitioner resources (Practitioner or PractitionerRole).
	"""
	
	device = "device"
	""" Group contains Device resources.
	"""
	
	medication = "medication"
	""" Group contains Medication resources.
	"""
	
	substance = "substance"
	""" Group contains Substance resources.
	"""
}


class GuidanceResponseStatus(object) {
	""" The status of a guidance response.

	URL: http://hl7.org/fhir/guidance-response-status
	ValueSet: http://hl7.org/fhir/ValueSet/guidance-response-status
	"""
	
	success = "success"
	""" The request was processed successfully.
	"""
	
	dataRequested = "data-requested"
	""" The request was processed successfully, but more data may result in a more complete evaluation.
	"""
	
	dataRequired = "data-required"
	""" The request was processed, but more data is required to complete the evaluation.
	"""
	
	inProgress = "in-progress"
	""" The request is currently being processed.
	"""
	
	failure = "failure"
	""" The request was not processed successfully.
	"""
	
	enteredInError = "entered-in-error"
	""" The response was entered in error.
	"""
}


class GuidePageGeneration(object) {
	""" A code that indicates how the page is generated.

	URL: http://hl7.org/fhir/guide-page-generation
	ValueSet: http://hl7.org/fhir/ValueSet/guide-page-generation
	"""
	
	html = "html"
	""" Page is proper xhtml with no templating.  Will be brought across unchanged for standard post-processing.
	"""
	
	markdown = "markdown"
	""" Page is markdown with templating.  Will use the template to create a file that imports the markdown file prior
	/// to post-processing.
	"""
	
	xml = "xml"
	""" Page is xml with templating.  Will use the template to create a file that imports the source file and run the
	/// nominated XSLT transform (see parameters) if present prior to post-processing.
	"""
	
	generated = "generated"
	""" Page will be generated by the publication process - no source to bring across.
	"""
}


class GuideParameterCode(object) {
	""" Code of parameter that is input to the guide.

	URL: http://hl7.org/fhir/guide-parameter-code
	ValueSet: http://hl7.org/fhir/ValueSet/guide-parameter-code
	"""
	
	apply = "apply"
	""" If the value of this string 0..* parameter is one of the metadata fields then all conformance resources will
	/// have any specified [Resource].[field] overwritten with the ImplementationGuide.[field], where field is one of:
	/// version, date, status, publisher, contact, copyright, experimental, jurisdiction, useContext.
	"""
	
	pathResource = "path-resource"
	""" The value of this string 0..* parameter is a subfolder of the build context's location that is to be scanned to
	/// load resources. Scope is (if present) a particular resource type.
	"""
	
	pathPages = "path-pages"
	""" The value of this string 0..1 parameter is a subfolder of the build context's location that contains files that
	/// are part of the html content processed by the builder.
	"""
	
	pathTxCache = "path-tx-cache"
	""" The value of this string 0..1 parameter is a subfolder of the build context's location that is used as the
	/// terminology cache. If this is not present, the terminology cache is on the local system, not under version
	/// control.
	"""
	
	expansionParameter = "expansion-parameter"
	""" The value of this string 0..* parameter is a parameter (name=value) when expanding value sets for this
	/// implementation guide. This is particularly used to specify the versions of published terminologies such as
	/// SNOMED CT.
	"""
	
	ruleBrokenLinks = "rule-broken-links"
	""" The value of this string 0..1 parameter is either "warning" or "error" (default = "error"). If the value is
	/// "warning" then IG build tools allow the IG to be considered successfully build even when there is no internal
	/// broken links.
	"""
	
	generateXml = "generate-xml"
	""" The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in XML format. If
	/// not present, the Publication Tool decides whether to generate XML.
	"""
	
	generateJson = "generate-json"
	""" The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in JSON format. If
	/// not present, the Publication Tool decides whether to generate JSON.
	"""
	
	generateTurtle = "generate-turtle"
	""" The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in Turtle format.
	/// If not present, the Publication Tool decides whether to generate Turtle.
	"""
	
	htmlTemplate = "html-template"
	""" The value of this string singleton parameter is the name of the file to use as the builder template for each
	/// generated page (see templating).
	"""
}


class HL7Workgroup(object) {
	""" An HL7 administrative unit that owns artifacts in the FHIR specification.

	URL: http://terminology.hl7.org/CodeSystem/hl7-work-group
	ValueSet: http://hl7.org/fhir/ValueSet/hl7-work-group
	"""
	
	cbcc = "cbcc"
	""" Community Based Collaborative Care (http://www.hl7.org/Special/committees/cbcc/index.cfm).
	"""
	
	cds = "cds"
	""" Clinical Decision Support (http://www.hl7.org/Special/committees/dss/index.cfm).
	"""
	
	cqi = "cqi"
	""" Clinical Quality Information (http://www.hl7.org/Special/committees/cqi/index.cfm).
	"""
	
	cg = "cg"
	""" Clinical Genomics (http://www.hl7.org/Special/committees/clingenomics/index.cfm).
	"""
	
	dev = "dev"
	""" Health Care Devices (http://www.hl7.org/Special/committees/healthcaredevices/index.cfm).
	"""
	
	ehr = "ehr"
	""" Electronic Health Records (http://www.hl7.org/special/committees/ehr/index.cfm).
	"""
	
	fhir = "fhir"
	""" FHIR Infrastructure (http://www.hl7.org/Special/committees/fiwg/index.cfm).
	"""
	
	fm = "fm"
	""" Financial Management (http://www.hl7.org/Special/committees/fm/index.cfm).
	"""
	
	hsi = "hsi"
	""" Health Standards Integration (http://www.hl7.org/Special/committees/hsi/index.cfm).
	"""
	
	ii = "ii"
	""" Imaging Integration (http://www.hl7.org/Special/committees/imagemgt/index.cfm).
	"""
	
	inm = "inm"
	""" Infrastructure And Messaging (http://www.hl7.org/special/committees/inm/index.cfm).
	"""
	
	its = "its"
	""" Implementable Technology Specifications (http://www.hl7.org/special/committees/xml/index.cfm).
	"""
	
	mnm = "mnm"
	""" Modeling and Methodology (http://www.hl7.org/Special/committees/mnm/index.cfm).
	"""
	
	oo = "oo"
	""" Orders and Observations (http://www.hl7.org/Special/committees/orders/index.cfm).
	"""
	
	pa = "pa"
	""" Patient Administration (http://www.hl7.org/Special/committees/pafm/index.cfm).
	"""
	
	pc = "pc"
	""" Patient Care (http://www.hl7.org/Special/committees/patientcare/index.cfm).
	"""
	
	pher = "pher"
	""" Public Health and Emergency Response (http://www.hl7.org/Special/committees/pher/index.cfm).
	"""
	
	phx = "phx"
	""" Pharmacy (http://www.hl7.org/Special/committees/medication/index.cfm).
	"""
	
	brr = "brr"
	""" Biomedical Research and Regulation (http://www.hl7.org/Special/committees/rcrim/index.cfm).
	"""
	
	sd = "sd"
	""" Structured Documents (http://www.hl7.org/Special/committees/structure/index.cfm).
	"""
	
	sec = "sec"
	""" Security (http://www.hl7.org/Special/committees/secure/index.cfm).
	"""
	
	us = "us"
	""" US Realm Taskforce (http://wiki.hl7.org/index.php?title=US_Realm_Task_Force).
	"""
	
	vocab = "vocab"
	""" Vocabulary (http://www.hl7.org/Special/committees/Vocab/index.cfm).
	"""
	
	aid = "aid"
	""" Application Implementation and Design (http://www.hl7.org/Special/committees/java/index.cfm).
	"""
}


class HTTPVerb(object) {
	""" HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.

	URL: http://hl7.org/fhir/http-verb
	ValueSet: http://hl7.org/fhir/ValueSet/http-verb
	"""
	
	GET = "GET"
	""" HTTP GET Command.
	"""
	
	HEAD = "HEAD"
	""" HTTP HEAD Command.
	"""
	
	POST = "POST"
	""" HTTP POST Command.
	"""
	
	PUT = "PUT"
	""" HTTP PUT Command.
	"""
	
	DELETE = "DELETE"
	""" HTTP DELETE Command.
	"""
	
	PATCH = "PATCH"
	""" HTTP PATCH Command.
	"""
}


class HandlingConditionSet(object) {
	""" Set of handling instructions prior testing of the specimen.

	URL: http://terminology.hl7.org/CodeSystem/handling-condition
	ValueSet: http://hl7.org/fhir/ValueSet/handling-condition
	"""
	
	room = "room"
	""" room temperature.
	"""
	
	refrigerated = "refrigerated"
	""" refrigerated temperature.
	"""
	
	frozen = "frozen"
	""" frozen temperature.
	"""
}


class HumanNameAssemblyOrder(object) {
	""" A code that represents the preferred display order of the components of a human name.

	URL: http://terminology.hl7.org/CodeSystem/name-assembly-order
	"""
	
	NL1 = "NL1"
	""" NL1
	"""
	
	NL2 = "NL2"
	""" NL2
	"""
	
	NL3 = "NL3"
	""" NL3
	"""
	
	NL4 = "NL4"
	""" NL4
	"""
}


class ISO210892017HealthRecordLifecycleEvents(object) {
	""" Attached is vocabulary for the 27 record lifecycle events, as per ISO TS 21089-2017, Health Informatics - Trusted End-
to-End Information Flows, Section 3, Terms and Definitions (2017, at ISO Central Secretariat, passed ballot and ready
for publication).  This will also be included in the FHIR EHR Record Lifecycle Event Implementation Guide, balloted and
(to be) published with FHIR STU-3.

	URL: http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle
	"""
	
	access = "access"
	""" Occurs when an agent causes the system to obtain and open a record entry for inspection or review.
	"""
	
	hold = "hold"
	""" Occurs when an agent causes the system to tag or otherwise indicate special access management and suspension of
	/// record entry deletion/destruction, if deemed relevant to a lawsuit or which are reasonably anticipated to be
	/// relevant or to fulfill organizational policy under the legal doctrine of “duty to preserve”.
	"""
	
	amend = "amend"
	""" Occurs when an agent makes any change to record entry content currently residing in storage considered permanent
	/// (persistent).
	"""
	
	archive = "archive"
	""" Occurs when an agent causes the system to create and move archive artifacts containing record entry content,
	/// typically to long-term offline storage.
	"""
	
	attest = "attest"
	""" Occurs when an agent causes the system to capture the agent’s digital signature (or equivalent indication)
	/// during formal validation of record entry content.
	"""
	
	decrypt = "decrypt"
	""" Occurs when an agent causes the system to decode record entry content from a cipher.
	"""
	
	deidentify = "deidentify"
	""" Occurs when an agent causes the system to scrub record entry content to reduce the association between a set of
	/// identifying data and the data subject in a way that might or might not be reversible.
	"""
	
	deprecate = "deprecate"
	""" Occurs when an agent causes the system to tag record entry(ies) as obsolete, erroneous or untrustworthy, to warn
	/// against its future use.
	"""
	
	destroy = "destroy"
	""" Occurs when an agent causes the system to permanently erase record entry content from the system.
	"""
	
	disclose = "disclose"
	""" Occurs when an agent causes the system to release, transfer, provision access to, or otherwise divulge record
	/// entry content.
	"""
	
	encrypt = "encrypt"
	""" Occurs when an agent causes the system to encode record entry content in a cipher.
	"""
	
	extract = "extract"
	""" Occurs when an agent causes the system to selectively pull out a subset of record entry content, based on
	/// explicit criteria.
	"""
	
	link = "link"
	""" Occurs when an agent causes the system to connect related record entries.
	"""
	
	merge = "merge"
	""" Occurs when an agent causes the system to combine or join content from two or more record entries, resulting in
	/// a single logical record entry.
	"""
	
	originate = "originate"
	""" Occurs when an agent causes the system to: a) initiate capture of potential record content, and b) incorporate
	/// that content into the storage considered a permanent part of the health record.
	"""
	
	pseudonymize = "pseudonymize"
	""" Occurs when an agent causes the system to remove record entry content to reduce the association between a set of
	/// identifying data and the data subject in a way that may be reversible.
	"""
	
	reactivate = "reactivate"
	""" Occurs when an agent causes the system to recreate or restore full status to record entries previously deleted
	/// or deprecated.
	"""
	
	receive = "receive"
	""" Occurs when an agent causes the system to a) initiate capture of data content from elsewhere, and b) incorporate
	/// that content into the storage considered a permanent part of the health record.
	"""
	
	reidentify = "reidentify"
	""" Occurs when an agent causes the system to restore information to data that allows identification of information
	/// source and/or information subject.
	"""
	
	unhold = "unhold"
	""" Occurs when an agent causes the system to remove a tag or other cues for special access management had required
	/// to fulfill organizational policy under the legal doctrine of “duty to preserve”.
	"""
	
	report = "report"
	""" Occurs when an agent causes the system to produce and deliver record entry content in a particular form and
	/// manner.
	"""
	
	restore = "restore"
	""" Occurs when an agent causes the system to recreate record entries and their content from a previous created
	/// archive artefact.
	"""
	
	transform = "transform"
	""" Occurs when an agent causes the system to change the form, language or code system used to represent record
	/// entry content.
	"""
	
	transmit = "transmit"
	""" Occurs when an agent causes the system to send record entry content from one (EHR/PHR/other) system to another.
	"""
	
	unlink = "unlink"
	""" Occurs when an agent causes the system to disconnect two or more record entries previously connected, rendering
	/// them separate (disconnected) again.
	"""
	
	unmerge = "unmerge"
	""" Occurs when an agent causes the system to reverse a previous record entry merge operation, rendering them
	/// separate again.
	"""
	
	verify = "verify"
	""" Occurs when an agent causes the system to confirm compliance of data or data objects with regulations,
	/// requirements, specifications, or other imposed conditions based on organizational policy.
	"""
}


class IdentifierUse(object) {
	""" Identifies the purpose for this identifier, if known .

	URL: http://hl7.org/fhir/identifier-use
	ValueSet: http://hl7.org/fhir/ValueSet/identifier-use
	"""
	
	usual = "usual"
	""" The identifier recommended for display and use in real-world interactions.
	"""
	
	official = "official"
	""" The identifier considered to be most trusted for the identification of this item. Sometimes also known as
	/// "primary" and "main". The determination of "official" is subjective and implementation guides often provide
	/// additional guidelines for use.
	"""
	
	temp = "temp"
	""" A temporary identifier.
	"""
	
	secondary = "secondary"
	""" An identifier that was assigned in secondary use - it serves to identify the object in a relative context, but
	/// cannot be consistently assigned to the same object again in a different context.
	"""
	
	old = "old"
	""" The identifier id no longer considered valid, but may be relevant for search purposes.  E.g. Changes to
	/// identifier schemes, account merges, etc.
	"""
}


class IdentityAssuranceLevel(object) {
	""" The level of confidence that this link represents the same actual person, based on NIST Authentication Levels.

	URL: http://hl7.org/fhir/identity-assuranceLevel
	ValueSet: http://hl7.org/fhir/ValueSet/identity-assuranceLevel
	"""
	
	level1 = "level1"
	""" Little or no confidence in the asserted identity's accuracy.
	"""
	
	level2 = "level2"
	""" Some confidence in the asserted identity's accuracy.
	"""
	
	level3 = "level3"
	""" High confidence in the asserted identity's accuracy.
	"""
	
	level4 = "level4"
	""" Very high confidence in the asserted identity's accuracy.
	"""
}


class ImagingStudyStatus(object) {
	""" The status of the ImagingStudy.

	URL: http://hl7.org/fhir/imagingstudy-status
	ValueSet: http://hl7.org/fhir/ValueSet/imagingstudy-status
	"""
	
	registered = "registered"
	""" The existence of the imaging study is registered, but there is nothing yet available.
	"""
	
	available = "available"
	""" At least one instance has been associated with this imaging study.
	"""
	
	cancelled = "cancelled"
	""" The imaging study is unavailable because the imaging study was not started or not completed (also sometimes
	/// called "aborted").
	"""
	
	enteredInError = "entered-in-error"
	""" The imaging study has been withdrawn following a previous final release.  This electronic record should never
	/// have existed, though it is possible that real-world decisions were based on it. (If real-world activity has
	/// occurred, the status should be "cancelled" rather than "entered-in-error".).
	"""
	
	unknown = "unknown"
	""" The system does not know which of the status values currently applies for this request. Note: This concept is
	/// not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known which one.
	"""
}


class ImplantStatus(object) {
	""" A set codes that define the functional status of an implanted device.

	URL: http://terminology.hl7.org/CodeSystem/implantStatus
	ValueSet: http://hl7.org/fhir/ValueSet/implantStatus
	"""
	
	functional = "functional"
	""" The implanted device is working normally.
	"""
	
	nonFunctional = "non-functional"
	""" The implanted device is not working.
	"""
	
	disabled = "disabled"
	""" The implanted device has been turned off.
	"""
	
	unknown = "unknown"
	""" the functional status of the implant has not been determined.
	"""
}


class InvoicePriceComponentType(object) {
	""" Codes indicating the kind of the price component.

	URL: http://hl7.org/fhir/invoice-priceComponentType
	ValueSet: http://hl7.org/fhir/ValueSet/invoice-priceComponentType
	"""
	
	base = "base"
	""" the amount is the base price used for calculating the total price before applying surcharges, discount or taxes.
	"""
	
	surcharge = "surcharge"
	""" the amount is a surcharge applied on the base price.
	"""
	
	deduction = "deduction"
	""" the amount is a deduction applied on the base price.
	"""
	
	discount = "discount"
	""" the amount is a discount applied on the base price.
	"""
	
	tax = "tax"
	""" the amount is the tax component of the total price.
	"""
	
	informational = "informational"
	""" the amount is of informational character, it has not been applied in the calculation of the total price.
	"""
}


class InvoiceStatus(object) {
	""" Codes identifying the lifecycle stage of an Invoice.

	URL: http://hl7.org/fhir/invoice-status
	ValueSet: http://hl7.org/fhir/ValueSet/invoice-status
	"""
	
	draft = "draft"
	""" the invoice has been prepared but not yet finalized.
	"""
	
	issued = "issued"
	""" the invoice has been finalized and sent to the recipient.
	"""
	
	balanced = "balanced"
	""" the invoice has been balaced / completely paid.
	"""
	
	cancelled = "cancelled"
	""" the invoice was cancelled.
	"""
	
	enteredInError = "entered-in-error"
	""" the invoice was determined as entered in error before it was issued.
	"""
}


class IssueSeverity(object) {
	""" How the issue affects the success of the action.

	URL: http://hl7.org/fhir/issue-severity
	ValueSet: http://hl7.org/fhir/ValueSet/issue-severity
	"""
	
	fatal = "fatal"
	""" The issue caused the action to fail and no further checking could be performed.
	"""
	
	error = "error"
	""" The issue is sufficiently important to cause the action to fail.
	"""
	
	warning = "warning"
	""" The issue is not important enough to cause the action to fail but may cause it to be performed suboptimally or
	/// in a way that is not as desired.
	"""
	
	information = "information"
	""" The issue has no relation to the degree of success of the action.
	"""
}


class IssueType(object) {
	""" A code that describes the type of issue.

	URL: http://hl7.org/fhir/issue-type
	ValueSet: http://hl7.org/fhir/ValueSet/issue-type
	"""
	
	invalid = "invalid"
	""" Content invalid against the specification or a profile.
	"""
	
	structure = "structure"
	""" A structural issue in the content such as wrong namespace, or unable to parse the content completely, or invalid
	/// json syntax.
	"""
	
	required = "required"
	""" A required element is missing.
	"""
	
	value = "value"
	""" An element or header value is invalid.
	"""
	
	invariant = "invariant"
	""" A content validation rule failed - e.g. a schematron rule.
	"""
	
	security = "security"
	""" An authentication/authorization/permissions issue of some kind.
	"""
	
	login = "login"
	""" The client needs to initiate an authentication process.
	"""
	
	unknown = "unknown"
	""" The user or system was not able to be authenticated (either there is no process, or the proferred token is
	/// unacceptable).
	"""
	
	expired = "expired"
	""" User session expired; a login may be required.
	"""
	
	forbidden = "forbidden"
	""" The user does not have the rights to perform this action.
	"""
	
	suppressed = "suppressed"
	""" Some information was not or might not have been returned due to business rules, consent or privacy rules, or
	/// access permission constraints.  This information may be accessible through alternate processes.
	"""
	
	processing = "processing"
	""" Processing issues. These are expected to be final e.g. there is no point resubmitting the same content
	/// unchanged.
	"""
	
	notSupported = "not-supported"
	""" The interaction, operation, resource or profile is not supported.
	"""
	
	duplicate = "duplicate"
	""" An attempt was made to create a duplicate record.
	"""
	
	multipleMatches = "multiple-matches"
	""" Multiple matching records were found when the operation required only one match.
	"""
	
	notFound = "not-found"
	""" The reference provided was not found. In a pure RESTful environment, this would be an HTTP 404 error, but this
	/// code may be used where the content is not found further into the application architecture.
	"""
	
	deleted = "deleted"
	""" The reference pointed to content (usually a resource) that has been deleted.
	"""
	
	tooLong = "too-long"
	""" Provided content is too long (typically, this is a denial of service protection type of error).
	"""
	
	codeInvalid = "code-invalid"
	""" The code or system could not be understood, or it was not valid in the context of a particular ValueSet.code.
	"""
	
	extension = "extension"
	""" An extension was found that was not acceptable, could not be resolved, or a modifierExtension was not
	/// recognized.
	"""
	
	tooCostly = "too-costly"
	""" The operation was stopped to protect server resources; e.g. a request for a value set expansion on all of SNOMED
	/// CT.
	"""
	
	businessRule = "business-rule"
	""" The content/operation failed to pass some business rule and so could not proceed.
	"""
	
	conflict = "conflict"
	""" Content could not be accepted because of an edit conflict (i.e. version aware updates). (In a pure RESTful
	/// environment, this would be an HTTP 409 error, but this code may be used where the conflict is discovered further
	/// into the application architecture.).
	"""
	
	transient = "transient"
	""" Transient processing issues. The system receiving the error may be able to resubmit the same content once an
	/// underlying issue is resolved.
	"""
	
	lockError = "lock-error"
	""" A resource/record locking failure (usually in an underlying database).
	"""
	
	noStore = "no-store"
	""" The persistent store is unavailable; e.g. the database is down for maintenance or similar action, and the
	/// interaction or operation cannot be processed.
	"""
	
	exception = "exception"
	""" y.
	"""
	
	timeout = "timeout"
	""" An internal timeout has occurred.
	"""
	
	incomplete = "incomplete"
	""" Not all data sources typically accessed could be reached or responded in time, so the returned information might
	/// not be complete (applies to search interactions and some operations).
	"""
	
	throttled = "throttled"
	""" The system is not prepared to handle this request due to load management.
	"""
	
	informational = "informational"
	""" A message unrelated to the processing success of the completed operation (examples of the latter include things
	/// like reminders of password expiry, system maintenance times, etc.).
	"""
}


class KnowledgeResourceType(object) {
	""" A list of all the knowledge resource types defined in this version of the FHIR specification.

	URL: http://hl7.org/fhir/knowledge-resource-types
	ValueSet: http://hl7.org/fhir/ValueSet/knowledge-resource-types
	"""
	
	activityDefinition = "ActivityDefinition"
	""" The definition of a specific activity to be taken, independent of any particular patient or context.
	"""
	
	codeSystem = "CodeSystem"
	""" A set of codes drawn from one or more code systems.
	"""
	
	conceptMap = "ConceptMap"
	""" A map from one set of concepts to one or more other concepts.
	"""
	
	library = "Library"
	""" Represents a library of quality improvement components.
	"""
	
	measure = "Measure"
	""" A quality measure definition.
	"""
	
	planDefinition = "PlanDefinition"
	""" The definition of a plan for a series of actions, independent of any specific patient or context.
	"""
	
	structureDefinition = "StructureDefinition"
	""" Structural Definition.
	"""
	
	structureMap = "StructureMap"
	""" A Map of relationships between 2 structures that can be used to transform data.
	"""
	
	valueSet = "ValueSet"
	""" A set of codes drawn from one or more code systems.
	"""
}


class LibraryType(object) {
	""" The type of knowledge asset this library contains.

	URL: http://terminology.hl7.org/CodeSystem/library-type
	ValueSet: http://hl7.org/fhir/ValueSet/library-type
	"""
	
	logicLibrary = "logic-library"
	""" The resource is a shareable library of formalized knowledge.
	"""
	
	modelDefinition = "model-definition"
	""" The resource is a definition of an information model.
	"""
	
	assetCollection = "asset-collection"
	""" The resource is a collection of knowledge assets.
	"""
	
	moduleDefinition = "module-definition"
	""" The resource defines the dependencies, parameters, and data requirements for a particular module or evaluation
	/// context.
	"""
}


class LinkType(object) {
	""" The type of link between this patient resource and another patient resource.

	URL: http://hl7.org/fhir/link-type
	ValueSet: http://hl7.org/fhir/ValueSet/link-type
	"""
	
	replacedBy = "replaced-by"
	""" The patient resource containing this link must no longer be used. The link points forward to another patient
	/// resource that must be used in lieu of the patient resource that contains this link.
	"""
	
	replaces = "replaces"
	""" The patient resource containing this link is the current active patient record. The link points back to an
	/// inactive patient resource that has been merged into this resource, and should be consulted to retrieve
	/// additional referenced information.
	"""
	
	refer = "refer"
	""" The patient resource containing this link is in use and valid but not considered the main source of information
	/// about a patient. The link points forward to another patient resource that should be consulted to retrieve
	/// additional patient information.
	"""
	
	seealso = "seealso"
	""" The patient resource containing this link is in use and valid, but points to another patient resource that is
	/// known to contain data about the same person. Data in this resource might overlap or contradict information found
	/// in the other patient resource. This link does not indicate any relative importance of the resources concerned,
	/// and both should be regarded as equally valid.
	"""
}


class LinkageType(object) {
	""" Used to distinguish different roles a resource can play within a set of linked resources.

	URL: http://hl7.org/fhir/linkage-type
	ValueSet: http://hl7.org/fhir/ValueSet/linkage-type
	"""
	
	source = "source"
	""" The record represents the "source of truth" (from the perspective of this Linkage resource) for the underlying
	/// event/condition/etc.
	"""
	
	alternate = "alternate"
	""" The record represents the alternative view of the underlying event/condition/etc.  The record may still be
	/// actively maintained, even though it is not considered to be the source of truth.
	"""
	
	historical = "historical"
	""" The record represents an obsolete record of the underlying event/condition/etc.  It is not expected to be
	/// actively maintained.
	"""
}


class ListMode(object) {
	""" The processing mode that applies to this list.

	URL: http://hl7.org/fhir/list-mode
	ValueSet: http://hl7.org/fhir/ValueSet/list-mode
	"""
	
	working = "working"
	""" This list is the master list, maintained in an ongoing fashion with regular updates as the real world list it is
	/// tracking changes.
	"""
	
	snapshot = "snapshot"
	""" This list was prepared as a snapshot. It should not be assumed to be current.
	"""
	
	changes = "changes"
	""" A point-in-time list that shows what changes have been made or recommended.  E.g. a discharge medication list
	/// showing what was added and removed during an encounter.
	"""
}


class ListStatus(object) {
	""" The current state of the list.

	URL: http://hl7.org/fhir/list-status
	ValueSet: http://hl7.org/fhir/ValueSet/list-status
	"""
	
	current = "current"
	""" The list is considered to be an active part of the patient's record.
	"""
	
	retired = "retired"
	""" The list is "old" and should no longer be considered accurate or relevant.
	"""
	
	enteredInError = "entered-in-error"
	""" The list was never accurate.  It is retained for medico-legal purposes only.
	"""
}


class LocationMode(object) {
	""" Indicates whether a resource instance represents a specific location or a class of locations.

	URL: http://hl7.org/fhir/location-mode
	ValueSet: http://hl7.org/fhir/ValueSet/location-mode
	"""
	
	instance = "instance"
	""" The Location resource represents a specific instance of a location (e.g. Operating Theatre 1A).
	"""
	
	kind = "kind"
	""" The Location represents a class of locations (e.g. Any Operating Theatre) although this class of locations could
	/// be constrained within a specific boundary (such as organization, or parent location, address etc.).
	"""
}


class LocationStatus(object) {
	""" Indicates whether the location is still in use.

	URL: http://hl7.org/fhir/location-status
	ValueSet: http://hl7.org/fhir/ValueSet/location-status
	"""
	
	active = "active"
	""" The location is operational.
	"""
	
	suspended = "suspended"
	""" The location is temporarily closed.
	"""
	
	inactive = "inactive"
	""" The location is no longer used.
	"""
}


class MatchGrade(object) {
	""" A Master Patient Index (MPI) assessment of whether a candidate patient record is a match or not.

	URL: http://terminology.hl7.org/CodeSystem/match-grade
	ValueSet: http://hl7.org/fhir/ValueSet/match-grade
	"""
	
	certain = "certain"
	""" This record meets the matching criteria to be automatically considered as a full match.
	"""
	
	probable = "probable"
	""" This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required
	/// before using this as a match.
	"""
	
	possible = "possible"
	""" This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as
	/// a match.
	"""
	
	certainlyNot = "certainly-not"
	""" This record is known not to be a match. Note that usually non-matching records are not returned, but in some
	/// cases records previously or likely considered as a match may specifically be negated by the matching engine.
	"""
}


class MaxOccurs(object) {
	""" Flags an element as having unlimited repetitions.

	URL: http://terminology.hl7.org/CodeSystem/question-max-occurs
	ValueSet: http://hl7.org/fhir/ValueSet/question-max-occurs
	"""
	
	max = "*"
	""" Element can repeat an unlimited number of times.
	"""
}


class MeasureDataUsage(object) {
	""" The intended usage for supplemental data elements in the measure.

	URL: http://terminology.hl7.org/CodeSystem/measure-data-usage
	ValueSet: http://hl7.org/fhir/ValueSet/measure-data-usage
	"""
	
	supplementalData = "supplemental-data"
	""" The data is intended to be provided as additional information alongside the measure results.
	"""
	
	riskAdjustmentFactor = "risk-adjustment-factor"
	""" The data is intended to be used to calculate and apply a risk adjustment model for the measure.
	"""
}


class MeasureImprovementNotation(object) {
	""" Observation values that indicate what change in a measurement value or score is indicative of an improvement in the
measured item or scored issue.

	URL: http://terminology.hl7.org/CodeSystem/measure-improvement-notation
	ValueSet: http://hl7.org/fhir/ValueSet/measure-improvement-notation
	"""
	
	increase = "increase"
	""" Improvement is indicated as an increase in the score or measurement (e.g. Higher score indicates better
	/// quality).
	"""
	
	decrease = "decrease"
	""" Improvement is indicated as a decrease in the score or measurement (e.g. Lower score indicates better quality).
	"""
}


class MeasurePopulationType(object) {
	""" The type of population.

	URL: http://terminology.hl7.org/CodeSystem/measure-population
	ValueSet: http://hl7.org/fhir/ValueSet/measure-population
	"""
	
	initialPopulation = "initial-population"
	""" The initial population refers to all patients or events to be evaluated by a quality measure involving patients
	/// who share a common set of specified characterstics. All patients or events counted (for example, as numerator,
	/// as denominator) are drawn from the initial population.
	"""
	
	numerator = "numerator"
	""" The upper portion of a fraction used to calculate a rate, proportion, or ratio. Also called the measure focus,
	/// it is the target process, condition, event, or outcome. Numerator criteria are the processes or outcomes
	/// expected for each patient, or event defined in the denominator. A numerator statement describes the clinical
	/// action that satisfies the conditions of the measure.
	"""
	
	numeratorExclusion = "numerator-exclusion"
	""" Numerator exclusion criteria define patients or events to be removed from the numerator. Numerator exclusions
	/// are used in proportion and ratio measures to help narrow the numerator (for inverted measures).
	"""
	
	denominator = "denominator"
	""" The lower portion of a fraction used to calculate a rate, proportion, or ratio. The denominator can be the same
	/// as the initial population, or a subset of the initial population to further constrain the population for the
	/// purpose of the measure.
	"""
	
	denominatorExclusion = "denominator-exclusion"
	""" Denominator exclusion criteria define patients or events that should be removed from the denominator before
	/// determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to
	/// help narrow the denominator. For example, patients with bilateral lower extremity amputations would be listed as
	/// a denominator exclusion for a measure requiring foot exams.
	"""
	
	denominatorException = "denominator-exception"
	""" Denominator exceptions are conditions that should remove a patient or event from the denominator of a measure
	/// only if the numerator criteria are not met. Denominator exception allows for adjustment of the calculated score
	/// for those providers with higher risk populations. Denominator exception criteria are only used in proportion
	/// measures.
	"""
	
	measurePopulation = "measure-population"
	""" Measure population criteria define the patients or events for which the individual observation for the measure
	/// should be taken. Measure populations are used for continuous variable measures rather than numerator and
	/// denominator criteria.
	"""
	
	measurePopulationExclusion = "measure-population-exclusion"
	""" Measure population criteria define the patients or events that should be removed from the measure population
	/// before determining the outcome of one or more continuous variables defined for the measure observation. Measure
	/// population exclusion criteria are used within continuous variable measures to help narrow the measure
	/// population.
	"""
	
	measureObservation = "measure-observation"
	""" Defines the individual observation to be performed for each patient or event in the measure population. Measure
	/// observations for each case in the population are aggregated to determine the overall measure score for the
	/// population.
	"""
}


class MeasureReportStatus(object) {
	""" The status of the measure report.

	URL: http://hl7.org/fhir/measure-report-status
	ValueSet: http://hl7.org/fhir/ValueSet/measure-report-status
	"""
	
	complete = "complete"
	""" The report is complete and ready for use.
	"""
	
	pending = "pending"
	""" The report is currently being generated.
	"""
	
	error = "error"
	""" An error occurred attempting to generate the report.
	"""
}


class MeasureReportType(object) {
	""" The type of the measure report.

	URL: http://hl7.org/fhir/measure-report-type
	ValueSet: http://hl7.org/fhir/ValueSet/measure-report-type
	"""
	
	individual = "individual"
	""" An individual report that provides information on the performance for a given measure with respect to a single
	/// subject.
	"""
	
	subjectList = "subject-list"
	""" A subject list report that includes a listing of subjects that satisfied each population criteria in the
	/// measure.
	"""
	
	summary = "summary"
	""" A summary report that returns the number of members in each population criteria for the measure.
	"""
	
	dataCollection = "data-collection"
	""" A data collection report that contains data-of-interest for the measure.
	"""
}


class MeasureScoring(object) {
	""" The scoring type of the measure.

	URL: http://terminology.hl7.org/CodeSystem/measure-scoring
	ValueSet: http://hl7.org/fhir/ValueSet/measure-scoring
	"""
	
	proportion = "proportion"
	""" The measure score is defined using a proportion.
	"""
	
	ratio = "ratio"
	""" The measure score is defined using a ratio.
	"""
	
	continuousVariable = "continuous-variable"
	""" The score is defined by a calculation of some quantity.
	"""
	
	cohort = "cohort"
	""" The measure is a cohort definition.
	"""
}


class MeasureType(object) {
	""" The type of measure (includes codes from 2.16.840.1.113883.1.11.20368).

	URL: http://terminology.hl7.org/CodeSystem/measure-type
	ValueSet: http://hl7.org/fhir/ValueSet/measure-type
	"""
	
	process = "process"
	""" A measure which focuses on a process which leads to a certain outcome, meaning that a scientific basis exists
	/// for believing that the process, when executed well, will increase the probability of achieving a desired
	/// outcome.
	"""
	
	outcome = "outcome"
	""" A measure that indicates the result of the performance (or non-performance) of a function or process.
	"""
	
	structure = "structure"
	""" A measure that focuses on a health care provider's capacity, systems, and processes to provide high-quality
	/// care.
	"""
	
	patientReportedOutcome = "patient-reported-outcome"
	""" A measure that focuses on patient-reported information such as patient engagement or patient experience
	/// measures.
	"""
	
	composite = "composite"
	""" A measure that combines multiple component measures in to a single quality measure.
	"""
}


class MessageSignificanceCategory(object) {
	""" The impact of the content of a message.

	URL: http://hl7.org/fhir/message-significance-category
	ValueSet: http://hl7.org/fhir/ValueSet/message-significance-category
	"""
	
	consequence = "consequence"
	""" The message represents/requests a change that should not be processed more than once; e.g., making a booking for
	/// an appointment.
	"""
	
	currency = "currency"
	""" The message represents a response to query for current information. Retrospective processing is wrong and/or
	/// wasteful.
	"""
	
	notification = "notification"
	""" The content is not necessarily intended to be current, and it can be reprocessed, though there may be version
	/// issues created by processing old notifications.
	"""
}


class MessageTransport(object) {
	""" The protocol used for message transport.

	URL: http://terminology.hl7.org/CodeSystem/message-transport
	ValueSet: http://hl7.org/fhir/ValueSet/message-transport
	"""
	
	http = "http"
	""" The application sends or receives messages using HTTP POST (may be over http: or https:).
	"""
	
	ftp = "ftp"
	""" The application sends or receives messages using File Transfer Protocol.
	"""
	
	mllp = "mllp"
	""" The application sends or receives messages using HL7's Minimal Lower Level Protocol.
	"""
}


class MessageheaderResponseRequest(object) {
	""" HL7-defined table of codes which identify conditions under which acknowledgments are required to be returned in response
to a message.

	URL: http://hl7.org/fhir/messageheader-response-request
	ValueSet: http://hl7.org/fhir/ValueSet/messageheader-response-request
	"""
	
	always = "always"
	""" initiator expects a response for this message.
	"""
	
	onError = "on-error"
	""" initiator expects a response only if in error.
	"""
	
	never = "never"
	""" initiator does not expect a response.
	"""
	
	onSuccess = "on-success"
	""" initiator expects a response only if successful.
	"""
}


class NHINPurposeOfUse(object) {
	""" This value set is suitable for use with the provenance resource. It is derived from, but not compatible with, the HL7 v3
Purpose of use Code system.

	URL: http://healthit.gov/nhin/purposeofuse
	ValueSet: http://hl7.org/fhir/ValueSet/nhin-purposeofuse
	"""
	
	TREATMENT = "TREATMENT"
	""" Treatment
	"""
	
	PAYMENT = "PAYMENT"
	""" Payment
	"""
	
	OPERATIONS = "OPERATIONS"
	""" Healthcare Operations
	"""
	
	SYSADMIN = "SYSADMIN"
	""" System Administration
	"""
	
	FRAUD = "FRAUD"
	""" Fraud detection
	"""
	
	PSYCHOTHERAPY = "PSYCHOTHERAPY"
	""" Use or disclosure of Psychotherapy Notes
	"""
	
	TRAINING = "TRAINING"
	""" Use or disclosure by the covered entity for its own training programs
	"""
	
	LEGAL = "LEGAL"
	""" Use or disclosure by the covered entity to defend itself in a legal action
	"""
	
	MARKETING = "MARKETING"
	""" Marketing
	"""
	
	DIRECTORY = "DIRECTORY"
	""" Use and disclosure for facility directories
	"""
	
	FAMILY = "FAMILY"
	""" Disclose to a family member, other relative, or a close personal friend of the individual
	"""
	
	PRESENT = "PRESENT"
	""" Uses and disclosures with the individual present.
	"""
	
	EMERGENCY = "EMERGENCY"
	""" Permission cannot practicably be provided because of the individual's incapacity or an emergency.
	"""
	
	DISASTER = "DISASTER"
	""" Use and disclosures for disaster relief purposes.
	"""
	
	PUBLICHEALTH = "PUBLICHEALTH"
	""" Uses and disclosures for public health activities.
	"""
	
	ABUSE = "ABUSE"
	""" Disclosures about victims of abuse, neglect or domestic violence.
	"""
	
	OVERSIGHT = "OVERSIGHT"
	""" Uses and disclosures for health oversight activities.
	"""
	
	JUDICIAL = "JUDICIAL"
	""" Disclosures for judicial and administrative proceedings.
	"""
	
	LAW = "LAW"
	""" Disclosures for law enforcement purposes.
	"""
	
	DECEASED = "DECEASED"
	""" Uses and disclosures about decedents.
	"""
	
	DONATION = "DONATION"
	""" Uses and disclosures for cadaveric organ,  eye or tissue donation purposes
	"""
	
	RESEARCH = "RESEARCH"
	""" Uses and disclosures for research purposes.
	"""
	
	THREAT = "THREAT"
	""" Uses and disclosures to avert a serious threat to health or safety.
	"""
	
	GOVERNMENT = "GOVERNMENT"
	""" Uses and disclosures for specialized government functions.
	"""
	
	WORKERSCOMP = "WORKERSCOMP"
	""" Disclosures for workers' compensation.
	"""
	
	COVERAGE = "COVERAGE"
	""" Disclosures for insurance or disability coverage determination
	"""
	
	REQUEST = "REQUEST"
	""" Request of the Individual
	"""
}


class NameUse(object) {
	""" The use of a human name.

	URL: http://hl7.org/fhir/name-use
	ValueSet: http://hl7.org/fhir/ValueSet/name-use
	"""
	
	usual = "usual"
	""" Known as/conventional/the one you normally use.
	"""
	
	official = "official"
	""" The formal name as registered in an official (government) registry, but which name might not be commonly used.
	/// May be called "legal name".
	"""
	
	temp = "temp"
	""" A temporary name. Name.period can provide more detailed information. This may also be used for temporary names
	/// assigned at birth or in emergency situations.
	"""
	
	nickname = "nickname"
	""" A name that is used to address the person in an informal manner, but is not part of their formal or usual name.
	"""
	
	anonymous = "anonymous"
	""" Anonymous assigned name, alias, or pseudonym (used to protect a person's identity for privacy reasons).
	"""
	
	old = "old"
	""" This name is no longer in use (or was never correct, but retained for records).
	"""
	
	maiden = "maiden"
	""" A name used prior to changing name because of marriage. This name use is for use by applications that collect
	/// and store names that were used prior to a marriage. Marriage naming customs vary greatly around the world, and
	/// are constantly changing. This term is not gender specific. The use of this term does not imply any particular
	/// history for a person's name.
	"""
}


class NamingSystemIdentifierType(object) {
	""" Identifies the style of unique identifier used to identify a namespace.

	URL: http://hl7.org/fhir/namingsystem-identifier-type
	ValueSet: http://hl7.org/fhir/ValueSet/namingsystem-identifier-type
	"""
	
	oid = "oid"
	""" An ISO object identifier; e.g. 1.2.3.4.5.
	"""
	
	uuid = "uuid"
	""" A universally unique identifier of the form a5afddf4-e880-459b-876e-e4591b0acc11.
	"""
	
	uri = "uri"
	""" A uniform resource identifier (ideally a URL - uniform resource locator); e.g. http://unitsofmeasure.org.
	"""
	
	other = "other"
	""" Some other type of unique identifier; e.g. HL7-assigned reserved string such as LN for LOINC.
	"""
}


class NamingSystemType(object) {
	""" Identifies the purpose of the naming system.

	URL: http://hl7.org/fhir/namingsystem-type
	ValueSet: http://hl7.org/fhir/ValueSet/namingsystem-type
	"""
	
	codesystem = "codesystem"
	""" The naming system is used to define concepts and symbols to represent those concepts; e.g. UCUM, LOINC, NDC
	/// code, local lab codes, etc.
	"""
	
	identifier = "identifier"
	""" The naming system is used to manage identifiers (e.g. license numbers, order numbers, etc.).
	"""
	
	root = "root"
	""" The naming system is used as the root for other identifiers and naming systems.
	"""
}


class NarrativeStatus(object) {
	""" The status of a resource narrative.

	URL: http://hl7.org/fhir/narrative-status
	ValueSet: http://hl7.org/fhir/ValueSet/narrative-status
	"""
	
	generated = "generated"
	""" The contents of the narrative are entirely generated from the core elements in the content.
	"""
	
	extensions = "extensions"
	""" The contents of the narrative are entirely generated from the core elements in the content and some of the
	/// content is generated from extensions. The narrative SHALL reflect the impact of all modifier extensions.
	"""
	
	additional = "additional"
	""" The contents of the narrative may contain additional information not found in the structured data. Note that
	/// there is no computable way to determine what the extra information is, other than by human inspection.
	"""
	
	empty = "empty"
	""" The contents of the narrative are some equivalent of "No human-readable text provided in this case".
	"""
}


class NoteType(object) {
	""" The presentation types of notes.

	URL: http://hl7.org/fhir/note-type
	ValueSet: http://hl7.org/fhir/ValueSet/note-type
	"""
	
	display = "display"
	""" Display the note.
	"""
	
	print = "print"
	""" Print the note on the form.
	"""
	
	printoper = "printoper"
	""" Print the note for the operator.
	"""
}


class ObservationDataType(object) {
	""" Permitted data type for observation value.

	URL: http://hl7.org/fhir/permitted-data-type
	ValueSet: http://hl7.org/fhir/ValueSet/permitted-data-type
	"""
	
	quantity = "Quantity"
	""" A measured amount.
	"""
	
	codeableConcept = "CodeableConcept"
	""" A coded concept from a reference terminology and/or text.
	"""
	
	string = "string"
	""" A sequence of Unicode characters.
	"""
	
	boolean = "boolean"
	""" true or false.
	"""
	
	integer = "integer"
	""" A signed integer.
	"""
	
	range = "Range"
	""" A set of values bounded by low and high.
	"""
	
	ratio = "Ratio"
	""" A ratio of two Quantity values - a numerator and a denominator.
	"""
	
	sampledData = "SampledData"
	""" A series of measurements taken by a device.
	"""
	
	time = "time"
	""" A time during the day, in the format hh:mm:ss.
	"""
	
	dateTime = "dateTime"
	""" A date, date-time or partial date (e.g. just year or year + month) as used in human communication.
	"""
	
	period = "Period"
	""" A time range defined by start and end date/time.
	"""
}


class ObservationRangeCategory(object) {
	""" Codes identifying the category of observation range.

	URL: http://hl7.org/fhir/observation-range-category
	ValueSet: http://hl7.org/fhir/ValueSet/observation-range-category
	"""
	
	reference = "reference"
	""" Reference (Normal) Range for Ordinal and Continuous Observations.
	"""
	
	critical = "critical"
	""" Critical Range for Ordinal and Continuous Observations.
	"""
	
	absolute = "absolute"
	""" Absolute Range for Ordinal and Continuous Observations. Results outside this range are not possible.
	"""
}


class ObservationStatus(object) {
	""" Codes providing the status of an observation.

	URL: http://hl7.org/fhir/observation-status
	ValueSet: http://hl7.org/fhir/ValueSet/observation-status
	"""
	
	registered = "registered"
	""" The existence of the observation is registered, but there is no result yet available.
	"""
	
	preliminary = "preliminary"
	""" This is an initial or interim observation: data may be incomplete or unverified.
	"""
	
	final = "final"
	""" The observation is complete and there are no further actions needed. Additional information such "released",
	/// "signed", etc would be represented using [Provenance](provenance.html) which provides not only the act but also
	/// the actors and dates and other related data. These act states would be associated with an observation status of
	/// `preliminary` until they are all completed and then a status of `final` would be applied.
	"""
	
	amended = "amended"
	""" Subsequent to being Final, the observation has been modified subsequent.  This includes updates/new information
	/// and corrections.
	"""
	
	corrected = "corrected"
	""" Subsequent to being Final, the observation has been modified to correct an error in the test result.
	"""
	
	cancelled = "cancelled"
	""" The observation is unavailable because the measurement was not started or not completed (also sometimes called
	/// "aborted").
	"""
	
	enteredInError = "entered-in-error"
	""" The observation has been withdrawn following previous final release.  This electronic record should never have
	/// existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred,
	/// the status should be "cancelled" rather than "entered-in-error".).
	"""
	
	unknown = "unknown"
	""" The authoring/source system does not know which of the status values currently applies for this observation.
	/// Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the
	/// authoring/source system does not know which.
	"""
}


class OperationKind(object) {
	""" Whether an operation is a normal operation or a query.

	URL: http://hl7.org/fhir/operation-kind
	ValueSet: http://hl7.org/fhir/ValueSet/operation-kind
	"""
	
	operation = "operation"
	""" This operation is invoked as an operation.
	"""
	
	query = "query"
	""" This operation is a named query, invoked using the search mechanism.
	"""
}


class OperationOutcomeCodes(object) {
	""" Operation Outcome codes used by FHIR test servers (see Implementation file translations.xml)

	URL: http://terminology.hl7.org/CodeSystem/operation-outcome
	"""
	
	DELETE_MULTIPLE_MATCHES = "DELETE_MULTIPLE_MATCHES"
	""" DELETE_MULTIPLE_MATCHES
	"""
	
	MSG_AUTH_REQUIRED = "MSG_AUTH_REQUIRED"
	""" MSG_AUTH_REQUIRED
	"""
	
	MSG_BAD_FORMAT = "MSG_BAD_FORMAT"
	""" MSG_BAD_FORMAT
	"""
	
	MSG_BAD_SYNTAX = "MSG_BAD_SYNTAX"
	""" MSG_BAD_SYNTAX
	"""
	
	MSG_CANT_PARSE_CONTENT = "MSG_CANT_PARSE_CONTENT"
	""" MSG_CANT_PARSE_CONTENT
	"""
	
	MSG_CANT_PARSE_ROOT = "MSG_CANT_PARSE_ROOT"
	""" MSG_CANT_PARSE_ROOT
	"""
	
	MSG_CREATED = "MSG_CREATED"
	""" MSG_CREATED
	"""
	
	MSG_DATE_FORMAT = "MSG_DATE_FORMAT"
	""" MSG_DATE_FORMAT
	"""
	
	MSG_DELETED = "MSG_DELETED"
	""" MSG_DELETED
	"""
	
	MSG_DELETED_DONE = "MSG_DELETED_DONE"
	""" MSG_DELETED_DONE
	"""
	
	MSG_DELETED_ID = "MSG_DELETED_ID"
	""" MSG_DELETED_ID
	"""
	
	MSG_DUPLICATE_ID = "MSG_DUPLICATE_ID"
	""" MSG_DUPLICATE_ID
	"""
	
	MSG_ERROR_PARSING = "MSG_ERROR_PARSING"
	""" MSG_ERROR_PARSING
	"""
	
	MSG_ID_INVALID = "MSG_ID_INVALID"
	""" MSG_ID_INVALID
	"""
	
	MSG_ID_TOO_LONG = "MSG_ID_TOO_LONG"
	""" MSG_ID_TOO_LONG
	"""
	
	MSG_INVALID_ID = "MSG_INVALID_ID"
	""" MSG_INVALID_ID
	"""
	
	MSG_JSON_OBJECT = "MSG_JSON_OBJECT"
	""" MSG_JSON_OBJECT
	"""
	
	MSG_LOCAL_FAIL = "MSG_LOCAL_FAIL"
	""" MSG_LOCAL_FAIL
	"""
	
	MSG_NO_EXIST = "MSG_NO_EXIST"
	""" MSG_NO_EXIST
	"""
	
	MSG_NO_MATCH = "MSG_NO_MATCH"
	""" MSG_NO_MATCH
	"""
	
	MSG_NO_MODULE = "MSG_NO_MODULE"
	""" MSG_NO_MODULE
	"""
	
	MSG_NO_SUMMARY = "MSG_NO_SUMMARY"
	""" MSG_NO_SUMMARY
	"""
	
	MSG_OP_NOT_ALLOWED = "MSG_OP_NOT_ALLOWED"
	""" MSG_OP_NOT_ALLOWED
	"""
	
	MSG_PARAM_CHAINED = "MSG_PARAM_CHAINED"
	""" MSG_PARAM_CHAINED
	"""
	
	MSG_PARAM_INVALID = "MSG_PARAM_INVALID"
	""" MSG_PARAM_INVALID
	"""
	
	MSG_PARAM_MODIFIER_INVALID = "MSG_PARAM_MODIFIER_INVALID"
	""" MSG_PARAM_MODIFIER_INVALID
	"""
	
	MSG_PARAM_NO_REPEAT = "MSG_PARAM_NO_REPEAT"
	""" MSG_PARAM_NO_REPEAT
	"""
	
	MSG_PARAM_UNKNOWN = "MSG_PARAM_UNKNOWN"
	""" MSG_PARAM_UNKNOWN
	"""
	
	MSG_RESOURCE_EXAMPLE_PROTECTED = "MSG_RESOURCE_EXAMPLE_PROTECTED"
	""" MSG_RESOURCE_EXAMPLE_PROTECTED
	"""
	
	MSG_RESOURCE_ID_FAIL = "MSG_RESOURCE_ID_FAIL"
	""" MSG_RESOURCE_ID_FAIL
	"""
	
	MSG_RESOURCE_ID_MISMATCH = "MSG_RESOURCE_ID_MISMATCH"
	""" MSG_RESOURCE_ID_MISMATCH
	"""
	
	MSG_RESOURCE_ID_MISSING = "MSG_RESOURCE_ID_MISSING"
	""" MSG_RESOURCE_ID_MISSING
	"""
	
	MSG_RESOURCE_NOT_ALLOWED = "MSG_RESOURCE_NOT_ALLOWED"
	""" MSG_RESOURCE_NOT_ALLOWED
	"""
	
	MSG_RESOURCE_REQUIRED = "MSG_RESOURCE_REQUIRED"
	""" MSG_RESOURCE_REQUIRED
	"""
	
	MSG_RESOURCE_TYPE_MISMATCH = "MSG_RESOURCE_TYPE_MISMATCH"
	""" MSG_RESOURCE_TYPE_MISMATCH
	"""
	
	MSG_SORT_UNKNOWN = "MSG_SORT_UNKNOWN"
	""" MSG_SORT_UNKNOWN
	"""
	
	MSG_TRANSACTION_DUPLICATE_ID = "MSG_TRANSACTION_DUPLICATE_ID"
	""" MSG_TRANSACTION_DUPLICATE_ID
	"""
	
	MSG_TRANSACTION_MISSING_ID = "MSG_TRANSACTION_MISSING_ID"
	""" MSG_TRANSACTION_MISSING_ID
	"""
	
	MSG_UNHANDLED_NODE_TYPE = "MSG_UNHANDLED_NODE_TYPE"
	""" MSG_UNHANDLED_NODE_TYPE
	"""
	
	MSG_UNKNOWN_CONTENT = "MSG_UNKNOWN_CONTENT"
	""" MSG_UNKNOWN_CONTENT
	"""
	
	MSG_UNKNOWN_OPERATION = "MSG_UNKNOWN_OPERATION"
	""" MSG_UNKNOWN_OPERATION
	"""
	
	MSG_UNKNOWN_TYPE = "MSG_UNKNOWN_TYPE"
	""" MSG_UNKNOWN_TYPE
	"""
	
	MSG_UPDATED = "MSG_UPDATED"
	""" MSG_UPDATED
	"""
	
	MSG_VERSION_AWARE = "MSG_VERSION_AWARE"
	""" MSG_VERSION_AWARE
	"""
	
	MSG_VERSION_AWARE_CONFLICT = "MSG_VERSION_AWARE_CONFLICT"
	""" MSG_VERSION_AWARE_CONFLICT
	"""
	
	MSG_VERSION_AWARE_URL = "MSG_VERSION_AWARE_URL"
	""" MSG_VERSION_AWARE_URL
	"""
	
	MSG_WRONG_NS = "MSG_WRONG_NS"
	""" MSG_WRONG_NS
	"""
	
	SEARCH_MULTIPLE = "SEARCH_MULTIPLE"
	""" SEARCH_MULTIPLE
	"""
	
	SEARCH_NONE = "SEARCH_NONE"
	""" SEARCH_NONE
	"""
	
	UPDATE_MULTIPLE_MATCHES = "UPDATE_MULTIPLE_MATCHES"
	""" UPDATE_MULTIPLE_MATCHES
	"""
}


class OperationParameterUse(object) {
	""" Whether an operation parameter is an input or an output parameter.

	URL: http://hl7.org/fhir/operation-parameter-use
	ValueSet: http://hl7.org/fhir/ValueSet/operation-parameter-use
	"""
	
	in = "in"
	""" This is an input parameter.
	"""
	
	out = "out"
	""" This is an output parameter.
	"""
}


class OrientationType(object) {
	""" Type for orientation.

	URL: http://hl7.org/fhir/orientation-type
	ValueSet: http://hl7.org/fhir/ValueSet/orientation-type
	"""
	
	sense = "sense"
	""" Sense orientation of reference sequence.
	"""
	
	antisense = "antisense"
	""" Antisense orientation of reference sequence.
	"""
}


class ParticipantRequired(object) {
	""" Is the Participant required to attend the appointment.

	URL: http://hl7.org/fhir/participantrequired
	ValueSet: http://hl7.org/fhir/ValueSet/participantrequired
	"""
	
	required = "required"
	""" The participant is required to attend the appointment.
	"""
	
	optional = "optional"
	""" The participant may optionally attend the appointment.
	"""
	
	informationOnly = "information-only"
	""" The participant is excluded from the appointment, and might not be informed of the appointment taking place.
	/// (Appointment is about them, not for them - such as 2 doctors discussing results about a patient's test).
	"""
}


class ParticipationStatus(object) {
	""" The Participation status of an appointment.

	URL: http://hl7.org/fhir/participationstatus
	ValueSet: http://hl7.org/fhir/ValueSet/participationstatus
	"""
	
	accepted = "accepted"
	""" The participant has accepted the appointment.
	"""
	
	declined = "declined"
	""" The participant has declined the appointment and will not participate in the appointment.
	"""
	
	tentative = "tentative"
	""" The participant has  tentatively accepted the appointment. This could be automatically created by a system and
	/// requires further processing before it can be accepted. There is no commitment that attendance will occur.
	"""
	
	needsAction = "needs-action"
	""" The participant needs to indicate if they accept the appointment by changing this status to one of the other
	/// statuses.
	"""
}


class PayeeResourceType(object) {
	""" The type of payee Resource.

	URL: http://terminology.hl7.org/CodeSystem/resource-type-link
	ValueSet: http://hl7.org/fhir/ValueSet/resource-type-link
	"""
	
	organization = "organization"
	""" Organization resource.
	"""
	
	patient = "patient"
	""" Patient resource.
	"""
	
	practitioner = "practitioner"
	""" Practitioner resource.
	"""
	
	relatedperson = "relatedperson"
	""" RelatedPerson resource.
	"""
}


class PlanDefinitionType(object) {
	""" The type of PlanDefinition.

	URL: http://terminology.hl7.org/CodeSystem/plan-definition-type
	ValueSet: http://hl7.org/fhir/ValueSet/plan-definition-type
	"""
	
	orderSet = "order-set"
	""" A pre-defined and approved group of orders related to a particular clinical condition (e.g. hypertension
	/// treatment and monitoring) or stage of care (e.g. hospital admission to Coronary Care Unit). An order set is used
	/// as a checklist for the clinician when managing a patient with a specific condition. It is a structured
	/// collection of orders relevant to that condition and presented to the clinician in a computerized provider order
	/// entry (CPOE) system.
	"""
	
	clinicalProtocol = "clinical-protocol"
	""" Defines a desired/typical sequence of clinical activities including preconditions, triggers and temporal
	/// relationships.
	"""
	
	ecaRule = "eca-rule"
	""" A decision support rule of the form [on Event] if Condition then Action. It is intended to be a shareable,
	/// computable definition of actions that should be taken whenever some condition is met in response to a particular
	/// event or events.
	"""
	
	workflowDefinition = "workflow-definition"
	""" Defines the steps for a group of one or more systems in an event flow process along with the step constraints,
	/// sequence, pre-conditions and decision points to complete a particular objective.
	"""
}


class PrecisionEstimateType(object) {
	""" Method of reporting variability of estimates, such as confidence intervals, interquartile range or standard deviation.

	URL: http://terminology.hl7.org/CodeSystem/precision-estimate-type
	ValueSet: http://hl7.org/fhir/ValueSet/precision-estimate-type
	"""
	
	CI = "CI"
	""" confidence interval.
	"""
	
	IQR = "IQR"
	""" interquartile range.
	"""
	
	SD = "SD"
	""" standard deviation.
	"""
	
	SE = "SE"
	""" standard error.
	"""
}


class PropertyRepresentation(object) {
	""" How a property is represented when serialized.

	URL: http://hl7.org/fhir/property-representation
	ValueSet: http://hl7.org/fhir/ValueSet/property-representation
	"""
	
	xmlAttr = "xmlAttr"
	""" In XML, this property is represented as an attribute not an element.
	"""
	
	xmlText = "xmlText"
	""" This element is represented using the XML text attribute (primitives only).
	"""
	
	typeAttr = "typeAttr"
	""" The type of this element is indicated using xsi:type.
	"""
	
	cdaText = "cdaText"
	""" Use CDA narrative instead of XHTML.
	"""
	
	xhtml = "xhtml"
	""" The property is represented using XHTML.
	"""
}


class PropertyType(object) {
	""" The type of a property value.

	URL: http://hl7.org/fhir/concept-property-type
	ValueSet: http://hl7.org/fhir/ValueSet/concept-property-type
	"""
	
	code = "code"
	""" The property value is a code that identifies a concept defined in the code system.
	"""
	
	coding = "Coding"
	""" The property  value is a code defined in an external code system. This may be used for translations, but is not
	/// the intent.
	"""
	
	string = "string"
	""" The property value is a string.
	"""
	
	integer = "integer"
	""" The property value is a string (often used to assign ranking values to concepts for supporting score
	/// assessments).
	"""
	
	boolean = "boolean"
	""" The property value is a boolean true | false.
	"""
	
	dateTime = "dateTime"
	""" The property is a date or a date + time.
	"""
	
	decimal = "decimal"
	""" The property value is a decimal number.
	"""
}


class ProvenanceEntityRole(object) {
	""" How an entity was used in an activity.

	URL: http://hl7.org/fhir/provenance-entity-role
	ValueSet: http://hl7.org/fhir/ValueSet/provenance-entity-role
	"""
	
	derivation = "derivation"
	""" A transformation of an entity into another, an update of an entity resulting in a new one, or the construction
	/// of a new entity based on a pre-existing entity.
	"""
	
	revision = "revision"
	""" A derivation for which the resulting entity is a revised version of some original.
	"""
	
	quotation = "quotation"
	""" The repeat of (some or all of) an entity, such as text or image, by someone who might or might not be its
	/// original author.
	"""
	
	source = "source"
	""" A primary source for a topic refers to something produced by some agent with direct experience and knowledge
	/// about the topic, at the time of the topic's study, without benefit from hindsight.
	"""
	
	removal = "removal"
	""" A derivation for which the entity is removed from accessibility usually through the use of the Delete operation.
	"""
}


class PublicationStatus(object) {
	""" The lifecycle status of an artifact.

	URL: http://hl7.org/fhir/publication-status
	ValueSet: http://hl7.org/fhir/ValueSet/publication-status
	"""
	
	draft = "draft"
	""" This resource is still under development and is not yet considered to be ready for normal use.
	"""
	
	active = "active"
	""" This resource is ready for normal use.
	"""
	
	retired = "retired"
	""" This resource has been withdrawn or superseded and should no longer be used.
	"""
	
	unknown = "unknown"
	""" The authoring system does not know which of the status values currently applies for this resource.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
	"""
}


class QualityOfEvidenceRating(object) {
	""" A rating system that describes the quality of evidence such as the GRADE, DynaMed, or Oxford CEBM systems.

	URL: http://terminology.hl7.org/CodeSystem/evidence-quality
	ValueSet: http://hl7.org/fhir/ValueSet/evidence-quality
	"""
	
	high = "high"
	""" High quality evidence.
	"""
	
	moderate = "moderate"
	""" Moderate quality evidence.
	"""
	
	low = "low"
	""" Low quality evidence.
	"""
	
	veryLow = "very-low"
	""" Very low quality evidence.
	"""
}


class QualityType(object) {
	""" Type for quality report.

	URL: http://hl7.org/fhir/quality-type
	ValueSet: http://hl7.org/fhir/ValueSet/quality-type
	"""
	
	indel = "indel"
	""" INDEL Comparison.
	"""
	
	snp = "snp"
	""" SNP Comparison.
	"""
	
	unknown = "unknown"
	""" UNKNOWN Comparison.
	"""
}


class QuantityComparator(object) {
	""" How the Quantity should be understood and represented.

	URL: http://hl7.org/fhir/quantity-comparator
	ValueSet: http://hl7.org/fhir/ValueSet/quantity-comparator
	"""
	
	lt = "<"
	""" The actual value is less than the given value.
	"""
	
	lte = "<="
	""" The actual value is less than or equal to the given value.
	"""
	
	gte = ">="
	""" The actual value is greater than or equal to the given value.
	"""
	
	gt = ">"
	""" The actual value is greater than the given value.
	"""
}


class QuestionnaireItemOperator(object) {
	""" The criteria by which a question is enabled.

	URL: http://hl7.org/fhir/questionnaire-enable-operator
	ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-enable-operator
	"""
	
	exists = "exists"
	""" True if whether an answer exists is equal to the enableWhen answer (which must be a boolean).
	"""
	
	eq = "="
	""" True if whether at least one answer has a value that is equal to the enableWhen answer.
	"""
	
	 = "!="
	""" True if whether at least no answer has a value that is equal to the enableWhen answer.
	"""
	
	gt = ">"
	""" True if whether at least no answer has a value that is greater than the enableWhen answer.
	"""
	
	lt = "<"
	""" True if whether at least no answer has a value that is less than the enableWhen answer.
	"""
	
	gte = ">="
	""" True if whether at least no answer has a value that is greater or equal to the enableWhen answer.
	"""
	
	lte = "<="
	""" True if whether at least no answer has a value that is less or equal to the enableWhen answer.
	"""
}


class QuestionnaireItemType(object) {
	""" Distinguishes groups from questions and display text and indicates data type for questions.

	URL: http://hl7.org/fhir/item-type
	ValueSet: http://hl7.org/fhir/ValueSet/item-type
	"""
	
	group = "group"
	""" An item with no direct answer but should have at least one child item.
	"""
	
	display = "display"
	""" Text for display that will not capture an answer or have child items.
	"""
	
	question = "question"
	""" An item that defines a specific answer to be captured, and which may have child items. (the answer provided in
	/// the QuestionnaireResponse should be of the defined datatype).
	"""
	
	boolean = "boolean"
	""" Question with a yes/no answer (valueBoolean).
	"""
	
	decimal = "decimal"
	""" Question with is a real number answer (valueDecimal).
	"""
	
	integer = "integer"
	""" Question with an integer answer (valueInteger).
	"""
	
	date = "date"
	""" Question with a date answer (valueDate).
	"""
	
	dateTime = "dateTime"
	""" Question with a date and time answer (valueDateTime).
	"""
	
	time = "time"
	""" Question with a time (hour:minute:second) answer independent of date. (valueTime).
	"""
	
	string = "string"
	""" Question with a short (few words to short sentence) free-text entry answer (valueString).
	"""
	
	text = "text"
	""" Question with a long (potentially multi-paragraph) free-text entry answer (valueString).
	"""
	
	url = "url"
	""" Question with a URL (website, FTP site, etc.) answer (valueUri).
	"""
	
	choice = "choice"
	""" Question with a Coding drawn from a list of possible answers (specified in either the answerOption property, or
	/// via the valueset referenced in the answerValueSet property) as an answer (valueCoding).
	"""
	
	openChoice = "open-choice"
	""" Answer is a Coding drawn from a list of possible answers (as with the choice type) or a free-text entry in a
	/// string (valueCoding or valueString).
	"""
	
	attachment = "attachment"
	""" Question with binary content such as an image, PDF, etc. as an answer (valueAttachment).
	"""
	
	reference = "reference"
	""" Question with a reference to another resource (practitioner, organization, etc.) as an answer (valueReference).
	"""
	
	quantity = "quantity"
	""" Question with a combination of a numeric value and unit, potentially with a comparator (<, >, etc.) as an
	/// answer. (valueQuantity) There is an extension 'http://hl7.org/fhir/StructureDefinition/questionnaire-unit' that
	/// can be used to define what unit should be captured (or the unit that has a ucum conversion from the provided
	/// unit).
	"""
}


class QuestionnaireItemUsageMode(object) {
	""" Identifies the modes of usage of a questionnaire that should enable a particular questionnaire item.

	URL: http://terminology.hl7.org/CodeSystem/questionnaire-usage-mode
	ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-usage-mode
	"""
	
	captureDisplay = "capture-display"
	""" Render the item regardless of usage mode.
	"""
	
	capture = "capture"
	""" Render the item only when capturing data.
	"""
	
	display = "display"
	""" Render the item only when displaying a completed form.
	"""
	
	displayNonEmpty = "display-non-empty"
	""" Render the item only when displaying a completed form and the item has been answered (or has child items that
	/// have been answered).
	"""
	
	captureDisplayNonEmpty = "capture-display-non-empty"
	""" Render the item when capturing data or when displaying a completed form and the item has been answered (or has
	/// child items that have been answered).
	"""
}


class QuestionnaireResponseStatus(object) {
	""" Lifecycle status of the questionnaire response.

	URL: http://hl7.org/fhir/questionnaire-answers-status
	ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-answers-status
	"""
	
	inProgress = "in-progress"
	""" This QuestionnaireResponse has been partially filled out with answers but changes or additions are still
	/// expected to be made to it.
	"""
	
	completed = "completed"
	""" This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.
	"""
	
	amended = "amended"
	""" This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions
	/// have been made to it afterwards.
	"""
	
	enteredInError = "entered-in-error"
	""" This QuestionnaireResponse was entered in error and voided.
	"""
	
	stopped = "stopped"
	""" This QuestionnaireResponse has been partially filled out with answers but has been abandoned. It is unknown
	/// whether changes or additions are expected to be made to it.
	"""
}


class ReferenceHandlingPolicy(object) {
	""" A set of flags that defines how references are supported.

	URL: http://hl7.org/fhir/reference-handling-policy
	ValueSet: http://hl7.org/fhir/ValueSet/reference-handling-policy
	"""
	
	literal = "literal"
	""" The server supports and populates Literal references (i.e. using Reference.reference) where they are known (this
	/// code does not guarantee that all references are literal; see 'enforced').
	"""
	
	logical = "logical"
	""" The server allows logical references (i.e. using Reference.identifier).
	"""
	
	resolves = "resolves"
	""" The server will attempt to resolve logical references to literal references - i.e. converting
	/// Reference.identifier to Reference.reference (if resolution fails, the server may still accept resources; see
	/// logical).
	"""
	
	enforced = "enforced"
	""" The server enforces that references have integrity - e.g. it ensures that references can always be resolved.
	/// This is typically the case for clinical record systems, but often not the case for middleware/proxy systems.
	"""
	
	local = "local"
	""" The server does not support references that point to other servers.
	"""
}


class ReferenceVersionRules(object) {
	""" Whether a reference needs to be version specific or version independent, or whether either can be used.

	URL: http://hl7.org/fhir/reference-version-rules
	ValueSet: http://hl7.org/fhir/ValueSet/reference-version-rules
	"""
	
	either = "either"
	""" The reference may be either version independent or version specific.
	"""
	
	independent = "independent"
	""" The reference must be version independent.
	"""
	
	specific = "specific"
	""" The reference must be version specific.
	"""
}


class ReferralMethod(object) {
	""" The methods of referral can be used when referring to a specific HealthCareService resource.

	URL: http://terminology.hl7.org/CodeSystem/service-referral-method
	ValueSet: http://hl7.org/fhir/ValueSet/service-referral-method
	"""
	
	fax = "fax"
	""" Referrals may be accepted by fax.
	"""
	
	phone = "phone"
	""" Referrals may be accepted over the phone from a practitioner.
	"""
	
	elec = "elec"
	""" Referrals may be accepted via a secure messaging system. To determine the types of secure messaging systems
	/// supported, refer to the identifiers collection. Callers will need to understand the specific identifier system
	/// used to know that they are able to transmit messages.
	"""
	
	semail = "semail"
	""" Referrals may be accepted via a secure email. To send please encrypt with the services public key.
	"""
	
	mail = "mail"
	""" Referrals may be accepted via regular postage (or hand delivered).
	"""
}


class RejectionCriterion(object) {
	""" Criterion for rejection of the specimen by laboratory.

	URL: http://terminology.hl7.org/CodeSystem/rejection-criteria
	ValueSet: http://hl7.org/fhir/ValueSet/rejection-criteria
	"""
	
	hemolized = "hemolized"
	""" blood specimen hemolized.
	"""
	
	insufficient = "insufficient"
	""" insufficient quantity of specimen.
	"""
	
	broken = "broken"
	""" specimen container broken.
	"""
	
	clotted = "clotted"
	""" specimen clotted.
	"""
	
	wrongTemperature = "wrong-temperature"
	""" specimen temperature inappropriate.
	"""
}


class RelatedArtifactType(object) {
	""" The type of relationship to the related artifact.

	URL: http://hl7.org/fhir/related-artifact-type
	ValueSet: http://hl7.org/fhir/ValueSet/related-artifact-type
	"""
	
	documentation = "documentation"
	""" Additional documentation for the knowledge resource. This would include additional instructions on usage as well
	/// as additional information on clinical context or appropriateness.
	"""
	
	justification = "justification"
	""" A summary of the justification for the knowledge resource including supporting evidence, relevant guidelines, or
	/// other clinically important information. This information is intended to provide a way to make the justification
	/// for the knowledge resource available to the consumer of interventions or results produced by the knowledge
	/// resource.
	"""
	
	citation = "citation"
	""" Bibliographic citation for papers, references, or other relevant material for the knowledge resource. This is
	/// intended to allow for citation of related material, but that was not necessarily specifically prepared in
	/// connection with this knowledge resource.
	"""
	
	predecessor = "predecessor"
	""" The previous version of the knowledge resource.
	"""
	
	successor = "successor"
	""" The next version of the knowledge resource.
	"""
	
	derivedFrom = "derived-from"
	""" The knowledge resource is derived from the related artifact. This is intended to capture the relationship in
	/// which a particular knowledge resource is based on the content of another artifact, but is modified to capture
	/// either a different set of overall requirements, or a more specific set of requirements such as those involved in
	/// a particular institution or clinical setting.
	"""
	
	dependsOn = "depends-on"
	""" The knowledge resource depends on the given related artifact.
	"""
	
	composedOf = "composed-of"
	""" The knowledge resource is composed of the given related artifact.
	"""
}


class RepositoryType(object) {
	""" Type for access of external URI.

	URL: http://hl7.org/fhir/repository-type
	ValueSet: http://hl7.org/fhir/ValueSet/repository-type
	"""
	
	directlink = "directlink"
	""" When URL is clicked, the resource can be seen directly (by webpage or by download link format).
	"""
	
	openapi = "openapi"
	""" When the API method (e.g. [base_url]/[parameter]) related with the URL of the website is executed, the resource
	/// can be seen directly (usually in JSON or XML format).
	"""
	
	login = "login"
	""" When logged into the website, the resource can be seen.
	"""
	
	oauth = "oauth"
	""" When logged in and  follow the API in the website related with URL, the resource can be seen.
	"""
	
	other = "other"
	""" Some other complicated or particular way to get resource from URL.
	"""
}


class RequestIntent(object) {
	""" Codes indicating the degree of authority/intentionality associated with a request.

	URL: http://hl7.org/fhir/request-intent
	ValueSet: http://hl7.org/fhir/ValueSet/request-intent
	"""
	
	proposal = "proposal"
	""" The request is a suggestion made by someone/something that does not have an intention to ensure it occurs and
	/// without providing an authorization to act.
	"""
	
	plan = "plan"
	""" The request represents an intention to ensure something occurs without providing an authorization for others to
	/// act.
	"""
	
	directive = "directive"
	""" The request represents a legally binding instruction authored by a Patient or RelatedPerson.
	"""
	
	order = "order"
	""" The request represents a request/demand and authorization for action by a Practitioner.
	"""
	
	originalOrder = "original-order"
	""" The request represents an original authorization for action.
	"""
	
	reflexOrder = "reflex-order"
	""" The request represents an automatically generated supplemental authorization for action based on a parent
	/// authorization together with initial results of the action taken against that parent authorization.
	"""
	
	fillerOrder = "filler-order"
	""" The request represents the view of an authorization instantiated by a fulfilling system representing the details
	/// of the fulfiller's intention to act upon a submitted order.
	"""
	
	instanceOrder = "instance-order"
	""" An order created in fulfillment of a broader order that represents the authorization for a single activity
	/// occurrence.  E.g. The administration of a single dose of a drug.
	"""
	
	option = "option"
	""" The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or
	/// other constraints among a set of requests.  Refer to [[[RequestGroup]]] for additional information on how this
	/// status is used.
	"""
}


class RequestPriority(object) {
	""" Identifies the level of importance to be assigned to actioning the request.

	URL: http://hl7.org/fhir/request-priority
	ValueSet: http://hl7.org/fhir/ValueSet/request-priority
	"""
	
	routine = "routine"
	""" The request has normal priority.
	"""
	
	urgent = "urgent"
	""" The request should be actioned promptly - higher priority than routine.
	"""
	
	asap = "asap"
	""" The request should be actioned as soon as possible - higher priority than urgent.
	"""
	
	stat = "stat"
	""" The request should be actioned immediately - highest possible priority.  E.g. an emergency.
	"""
}


class RequestResourceType(object) {
	""" A list of all the request resource types defined in this version of the FHIR specification.

	URL: http://hl7.org/fhir/request-resource-types
	ValueSet: http://hl7.org/fhir/ValueSet/request-resource-types
	"""
	
	appointment = "Appointment"
	""" A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a
	/// specific date/time. This may result in one or more Encounter(s).
	"""
	
	appointmentResponse = "AppointmentResponse"
	""" A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
	"""
	
	carePlan = "CarePlan"
	""" Healthcare plan for patient or group.
	"""
	
	claim = "Claim"
	""" Claim, Pre-determination or Pre-authorization.
	"""
	
	communicationRequest = "CommunicationRequest"
	""" A request for information to be sent to a receiver.
	"""
	
	contract = "Contract"
	""" Legal Agreement.
	"""
	
	deviceRequest = "DeviceRequest"
	""" Medical device request.
	"""
	
	enrollmentRequest = "EnrollmentRequest"
	""" Enrollment request.
	"""
	
	immunizationRecommendation = "ImmunizationRecommendation"
	""" Guidance or advice relating to an immunization.
	"""
	
	medicationRequest = "MedicationRequest"
	""" Ordering of medication for patient or group.
	"""
	
	nutritionOrder = "NutritionOrder"
	""" Diet, formula or nutritional supplement request.
	"""
	
	serviceRequest = "ServiceRequest"
	""" A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
	"""
	
	supplyRequest = "SupplyRequest"
	""" Request for a medication, substance or device.
	"""
	
	task = "Task"
	""" A task to be performed.
	"""
	
	visionPrescription = "VisionPrescription"
	""" Prescription for vision correction products for a patient.
	"""
}


class RequestStatus(object) {
	""" Codes identifying the lifecycle stage of a request.

	URL: http://hl7.org/fhir/request-status
	ValueSet: http://hl7.org/fhir/ValueSet/request-status
	"""
	
	draft = "draft"
	""" The request has been created but is not yet complete or ready for action.
	"""
	
	active = "active"
	""" The request is in force and ready to be acted upon.
	"""
	
	onHold = "on-hold"
	""" The request (and any implicit authorization to act) has been temporarily withdrawn but is expected to resume in
	/// the future.
	"""
	
	revoked = "revoked"
	""" The request (and any implicit authorization to act) has been terminated prior to the known full completion of
	/// the intended actions.  No further activity should occur.
	"""
	
	completed = "completed"
	""" The activity described by the request has been fully performed.  No further activity will occur.
	"""
	
	enteredInError = "entered-in-error"
	""" This request should never have existed and should be considered 'void'.  (It is possible that real-world
	/// decisions were based on it.  If real-world activity has occurred, the status should be "cancelled" rather than
	/// "entered-in-error".).
	"""
	
	unknown = "unknown"
	""" The authoring system does not know which of the status values currently applies for this request.  Note: This
	/// concept is not to be used for "other" . One of the listed statuses is presumed to apply,  but the system
	/// creating the request does not know.
	"""
}


class ResearchElementType(object) {
	""" The possible types of research elements (E.g. Population, Exposure, Outcome).

	URL: http://hl7.org/fhir/research-element-type
	ValueSet: http://hl7.org/fhir/ValueSet/research-element-type
	"""
	
	population = "population"
	""" The element defines the population that forms the basis for research.
	"""
	
	exposure = "exposure"
	""" The element defines an exposure within the population that is being researched.
	"""
	
	outcome = "outcome"
	""" The element defines an outcome within the population that is being researched.
	"""
}


class ResearchStudyObjectiveType(object) {
	""" Codes for the kind of study objective.

	URL: http://terminology.hl7.org/CodeSystem/research-study-objective-type
	ValueSet: http://hl7.org/fhir/ValueSet/research-study-objective-type
	"""
	
	primary = "primary"
	""" The main question to be answered, and the one that drives any statistical planning for the study—e.g.,
	/// calculation of the sample size to provide the appropriate power for statistical testing.
	"""
	
	secondary = "secondary"
	""" Question to be answered in the study that is of lesser importance than the primary objective.
	"""
	
	exploratory = "exploratory"
	""" Exploratory questions to be answered in the study.
	"""
}


class ResearchStudyPhase(object) {
	""" Codes for the stage in the progression of a therapy from initial experimental use in humans in clinical trials to post-
market evaluation.

	URL: http://terminology.hl7.org/CodeSystem/research-study-phase
	ValueSet: http://hl7.org/fhir/ValueSet/research-study-phase
	"""
	
	NA = "n-a"
	""" Trials without phases (for example, studies of devices or behavioral interventions).
	"""
	
	earlyPhase1 = "early-phase-1"
	""" Designation for optional exploratory trials conducted in accordance with the United States Food and Drug
	/// Administration's (FDA) 2006 Guidance on Exploratory Investigational New Drug (IND) Studies. Formerly called
	/// Phase 0.
	"""
	
	phase1 = "phase-1"
	""" Includes initial studies to determine the metabolism and pharmacologic actions of drugs in humans, the side
	/// effects associated with increasing doses, and to gain early evidence of effectiveness; may include healthy
	/// participants and/or patients.
	"""
	
	phase1Phase2 = "phase-1-phase-2"
	""" Trials that are a combination of phases 1 and 2.
	"""
	
	phase2 = "phase-2"
	""" Includes controlled clinical studies conducted to evaluate the effectiveness of the drug for a particular
	/// indication or indications in participants with the disease or condition under study and to determine the common
	/// short-term side effects and risks.
	"""
	
	phase2Phase3 = "phase-2-phase-3"
	""" Trials that are a combination of phases 2 and 3.
	"""
	
	phase3 = "phase-3"
	""" Includes trials conducted after preliminary evidence suggesting effectiveness of the drug has been obtained, and
	/// are intended to gather additional information to evaluate the overall benefit-risk relationship of the drug.
	"""
	
	phase4 = "phase-4"
	""" Studies of FDA-approved drugs to delineate additional information including the drug's risks, benefits, and
	/// optimal use.
	"""
}


class ResearchStudyPrimaryPurposeType(object) {
	""" Codes for the main intent of the study.

	URL: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type
	ValueSet: http://hl7.org/fhir/ValueSet/research-study-prim-purp-type
	"""
	
	treatment = "treatment"
	""" One or more interventions are being evaluated for treating a disease, syndrome, or condition.
	"""
	
	prevention = "prevention"
	""" One or more interventions are being assessed for preventing the development of a specific disease or health
	/// condition.
	"""
	
	diagnostic = "diagnostic"
	""" One or more interventions are being evaluated for identifying a disease or health condition.
	"""
	
	supportiveCare = "supportive-care"
	""" One or more interventions are evaluated for maximizing comfort, minimizing side effects, or mitigating against a
	/// decline in the participant's health or function.
	"""
	
	screening = "screening"
	""" One or more interventions are assessed or examined for identifying a condition, or risk factors for a condition,
	/// in people who are not yet known to have the condition or risk factor.
	"""
	
	healthServicesResearch = "health-services-research"
	""" One or more interventions for evaluating the delivery, processes, management, organization, or financing of
	/// healthcare.
	"""
	
	basicScience = "basic-science"
	""" One or more interventions for examining the basic mechanism of action (for example, physiology or biomechanics
	/// of an intervention).
	"""
	
	deviceFeasibility = "device-feasibility"
	""" An intervention of a device product is being evaluated to determine the feasibility of the product or to test a
	/// prototype device and not health outcomes. Such studies are conducted to confirm the design and operating
	/// specifications of a device before beginning a full clinical trial.
	"""
}


class ResearchStudyReasonStopped(object) {
	""" Codes for why the study ended prematurely.

	URL: http://terminology.hl7.org/CodeSystem/research-study-reason-stopped
	ValueSet: http://hl7.org/fhir/ValueSet/research-study-reason-stopped
	"""
	
	accrualGoalMet = "accrual-goal-met"
	""" The study prematurely ended because the accrual goal was met.
	"""
	
	closedDueToToxicity = "closed-due-to-toxicity"
	""" The study prematurely ended due to toxicity.
	"""
	
	closedDueToLackOfStudyProgress = "closed-due-to-lack-of-study-progress"
	""" The study prematurely ended due to lack of study progress.
	"""
	
	temporarilyClosedPerStudyDesign = "temporarily-closed-per-study-design"
	""" The study prematurely ended temporarily per study design.
	"""
}


class ResearchStudyStatus(object) {
	""" Codes that convey the current status of the research study.

	URL: http://hl7.org/fhir/research-study-status
	ValueSet: http://hl7.org/fhir/ValueSet/research-study-status
	"""
	
	active = "active"
	""" Study is opened for accrual.
	"""
	
	administrativelyCompleted = "administratively-completed"
	""" Study is completed prematurely and will not resume; patients are no longer examined nor treated.
	/// Tagged.
	"""
	
	approved = "approved"
	""" Protocol is approved by the review board.
	"""
	
	closedToAccrual = "closed-to-accrual"
	""" Study is closed for accrual; patients can be examined and treated.
	"""
	
	closedToAccrualAndIntervention = "closed-to-accrual-and-intervention"
	""" Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment or intervention but are still being followed according to the primary objective of the
	/// study.
	"""
	
	completed = "completed"
	""" Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment
	/// or intervention but are still being followed according to the primary objective of the study.
	"""
	
	disapproved = "disapproved"
	""" Protocol was disapproved by the review board.
	"""
	
	inReview = "in-review"
	""" Protocol is submitted to the review board for approval.
	"""
	
	temporarilyClosedToAccrual = "temporarily-closed-to-accrual"
	""" Study is temporarily closed for accrual; can be potentially resumed in the future; patients can be examined and
	/// treated.
	"""
	
	temporarilyClosedToAccrualAndIntervention = "temporarily-closed-to-accrual-and-intervention"
	""" Study is temporarily closed for accrual and intervention and potentially can be resumed in the future.
	"""
	
	withdrawn = "withdrawn"
	""" Protocol was withdrawn by the lead organization.
	"""
}


class ResearchSubjectStatus(object) {
	""" Indicates the progression of a study subject through a study.

	URL: http://hl7.org/fhir/research-subject-status
	ValueSet: http://hl7.org/fhir/ValueSet/research-subject-status
	"""
	
	candidate = "candidate"
	""" An identified person that can be considered for inclusion in a study.
	"""
	
	eligible = "eligible"
	""" A person that has met the eligibility criteria for inclusion in a study.
	"""
	
	followUp = "follow-up"
	""" A person is no longer receiving study intervention and/or being evaluated with tests and procedures according to
	/// the protocol, but they are being monitored on a protocol-prescribed schedule.
	"""
	
	ineligible = "ineligible"
	""" A person who did not meet one or more criteria required for participation in a study is considered to have
	/// failed screening or
	/// is ineligible for the study.
	"""
	
	notRegistered = "not-registered"
	""" A person for whom registration was not completed.
	"""
	
	offStudy = "off-study"
	""" A person that has ended their participation on a study either because their treatment/observation is complete or
	/// through not
	/// responding, withdrawal, non-compliance and/or adverse event.
	"""
	
	onStudy = "on-study"
	""" A person that is enrolled or registered on a study.
	"""
	
	onStudyIntervention = "on-study-intervention"
	""" The person is receiving the treatment or participating in an activity (e.g. yoga, diet, etc.) that the study is
	/// evaluating.
	"""
	
	onStudyObservation = "on-study-observation"
	""" The subject is being evaluated via tests and assessments according to the study calendar, but is not receiving
	/// any intervention. Note that this state is study-dependent and might not exist in all studies.  A synonym for
	/// this is "short-term follow-up".
	"""
	
	pendingOnStudy = "pending-on-study"
	""" A person is pre-registered for a study.
	"""
	
	potentialCandidate = "potential-candidate"
	""" A person that is potentially eligible for participation in the study.
	"""
	
	screening = "screening"
	""" A person who is being evaluated for eligibility for a study.
	"""
	
	withdrawn = "withdrawn"
	""" The person has withdrawn their participation in the study before registration.
	"""
}


class ResourceSecurityCategory(object) {
	""" Provides general guidance around the kind of access Control to Read, Search, Create, Update, or Delete a resource.

	URL: http://terminology.hl7.org/CodeSystem/resource-security-category
	ValueSet: http://hl7.org/fhir/ValueSet/resource-security-category
	"""
	
	anonymous = "anonymous"
	""" These resources tend to not contain any individual data, or business sensitive data. Most often these Resources
	/// will be available for anonymous access, meaning there is no access control based on the user or system
	/// requesting. However these Resources do tend to contain important information that must be authenticated back to
	/// the source publishing them, and protected from integrity failures in communication. For this reason server
	/// authenticated https (TLS) is recommended to provide authentication of the server and integrity protection in
	/// transit. This is normal web-server use of https.
	"""
	
	business = "business"
	""" These Resources tend to not contain any individual data, but do have data that describe business or service
	/// sensitive data. The use of the term Business is not intended to only mean an incorporated business, but rather
	/// the more broad concept of an organization, location, or other group that is not identifable as individuals.
	/// Often these resources will require some for of client authentication to assure that only authorized access is
	/// given. The client access control may be to individuals, or may be to system identity. For this purpose possible
	/// client authentication methods such as: mutual-authenticated-TLS, APIKey, App signed JWT, or App OAuth client-id
	/// JWT For example: a App that uses a Business protected Provider Directory to determine other business endpoint
	/// details.
	"""
	
	individual = "individual"
	""" These Resources do NOT contain Patient data, but do contain individual information about other participants.
	/// These other individuals are Practitioners, PractionerRole, CareTeam, or other users. These identities are needed
	/// to enable the practice of healthcare. These identities are identities under general privacy regulations, and
	/// thus must consider Privacy risk. Often access to these other identities are covered by business relationships.
	/// For this purpose access to these Resources will tend to be Role specific using methods such as RBAC or ABAC.
	"""
	
	patient = "patient"
	""" These Resources make up the bulk of FHIR and therefore are the most commonly understood. These Resources contain
	/// highly sesitive health information, or are closely linked to highly sensitive health information. These
	/// Resources will often use the security labels to differentiate various confidentiality levels within this broad
	/// group of Patient Sensitive data. Access to these Resources often requires a declared Purpose Of Use. Access to
	/// these Resources is often controlled by a Privacy Consent.
	"""
	
	notClassified = "not-classified"
	""" Some Resources can be used for a wide scope of use-cases that span very sensitive to very non-sensitive. These
	/// Resources do not fall into any of the above classifications, as their sensitivity is highly variable. These
	/// Resources will need special handling. These Resources often contain metadata that describes the content in a way
	/// that can be used for Access Control decisions.
	"""
}


class ResourceType(object) {
	""" One of the resource types defined as part of this version of FHIR.

	URL: http://hl7.org/fhir/resource-types
	"""
	
	account = "Account"
	""" A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track
	/// charges for a patient, cost centers, etc.
	"""
	
	activityDefinition = "ActivityDefinition"
	""" This resource allows for the definition of some activity to be performed, independent of a particular patient,
	/// practitioner, or other performance context.
	"""
	
	adverseEvent = "AdverseEvent"
	""" Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by
	/// medical care, a research study or other healthcare setting factors that requires additional monitoring,
	/// treatment, or hospitalization, or that results in death.
	"""
	
	allergyIntolerance = "AllergyIntolerance"
	""" Risk of harmful or undesirable, physiological response which is unique to an individual and associated with
	/// exposure to a substance.
	"""
	
	appointment = "Appointment"
	""" A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a
	/// specific date/time. This may result in one or more Encounter(s).
	"""
	
	appointmentResponse = "AppointmentResponse"
	""" A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
	"""
	
	auditEvent = "AuditEvent"
	""" A record of an event made for purposes of maintaining a security log. Typical uses include detection of
	/// intrusion attempts and monitoring for inappropriate usage.
	"""
	
	basic = "Basic"
	""" Basic is used for handling concepts not yet defined in FHIR, narrative-only resources that don't map to an
	/// existing resource, and custom resources not appropriate for inclusion in the FHIR specification.
	"""
	
	binary = "Binary"
	""" A resource that represents the data of a single raw artifact as digital content accessible in its native format.
	/// A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
	"""
	
	biologicallyDerivedProduct = "BiologicallyDerivedProduct"
	""" A material substance originating from a biological entity intended to be transplanted or infused
	/// into another (possibly the same) biological entity.
	"""
	
	bodyStructure = "BodyStructure"
	""" Record details about an anatomical structure.  This resource may be used when a coded concept does not provide
	/// the necessary detail needed for the use case.
	"""
	
	bundle = "Bundle"
	""" A container for a collection of resources.
	"""
	
	capabilityStatement = "CapabilityStatement"
	""" A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of
	/// FHIR that may be used as a statement of actual server functionality or a statement of required or desired server
	/// implementation.
	"""
	
	carePlan = "CarePlan"
	""" Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group
	/// or community for a period of time, possibly limited to care for a specific condition or set of conditions.
	"""
	
	careTeam = "CareTeam"
	""" The Care Team includes all the people and organizations who plan to participate in the coordination and delivery
	/// of care for a patient.
	"""
	
	catalogEntry = "CatalogEntry"
	""" Catalog entries are wrappers that contextualize items included in a catalog.
	"""
	
	chargeItem = "ChargeItem"
	""" The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore
	/// referring not only to the product, but containing in addition details of the provision, like date, time, amounts
	/// and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and
	/// internal cost allocation.
	"""
	
	chargeItemDefinition = "ChargeItemDefinition"
	""" The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to
	/// calculate costs and prices. The properties may differ largely depending on type and realm, therefore this
	/// resource gives only a rough structure and requires profiling for each type of billing code system.
	"""
	
	claim = "Claim"
	""" A provider issued list of services and products provided, or to be provided, to a patient which is provided to
	/// an insurer for payment recovery.
	"""
	
	claimResponse = "ClaimResponse"
	""" This resource provides the adjudication details from the processing of a Claim resource.
	"""
	
	clinicalImpression = "ClinicalImpression"
	""" A record of a clinical assessment performed to determine what problem(s) may affect the patient and before
	/// planning the treatments or management strategies that are best to manage a patient's condition. Assessments are
	/// often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow.
	/// This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the
	/// recording of assessment tools such as Apgar score.
	"""
	
	codeSystem = "CodeSystem"
	""" The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement
	/// and its key properties, and optionally define a part or all of its content.
	"""
	
	communication = "Communication"
	""" An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public
	/// health agency was notified about a reportable condition.
	"""
	
	communicationRequest = "CommunicationRequest"
	""" A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider,
	/// the CDS system proposes that the public health agency be notified about a reportable condition.
	"""
	
	compartmentDefinition = "CompartmentDefinition"
	""" A compartment definition that defines how resources are accessed on a server.
	"""
	
	composition = "Composition"
	""" A set of healthcare-related information that is assembled together into a single logical package that provides a
	/// single coherent statement of meaning, establishes its own context and that has clinical attestation with regard
	/// to who is making the statement. A Composition defines the structure and narrative content necessary for a
	/// document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first
	/// entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be
	/// included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
	"""
	
	conceptMap = "ConceptMap"
	""" A statement of relationships from one set of concepts to one or more other concepts - either concepts in code
	/// systems, or data element/data element concepts, or classes in class models.
	"""
	
	condition = "Condition"
	""" A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen
	/// to a level of concern.
	"""
	
	consent = "Consent"
	""" A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient
	/// role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
	"""
	
	contract = "Contract"
	""" Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
	"""
	
	coverage = "Coverage"
	""" Financial instrument which may be used to reimburse or pay for health care products and services. Includes both
	/// insurance and self-payment.
	"""
	
	coverageEligibilityRequest = "CoverageEligibilityRequest"
	""" The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to
	/// respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage
	/// is valid and in-force and optionally to provide the insurance details of the policy.
	"""
	
	coverageEligibilityResponse = "CoverageEligibilityResponse"
	""" This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest
	/// resource.
	"""
	
	detectedIssue = "DetectedIssue"
	""" Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions
	/// for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
	"""
	
	device = "Device"
	""" A type of a manufactured item that is used in the provision of healthcare without being substantially changed
	/// through that activity. The device may be a medical or non-medical device.
	"""
	
	deviceDefinition = "DeviceDefinition"
	""" The characteristics, operational status and capabilities of a medical-related component of a medical device.
	"""
	
	deviceMetric = "DeviceMetric"
	""" Describes a measurement, calculation or setting capability of a medical device.
	"""
	
	deviceRequest = "DeviceRequest"
	""" Represents a request for a patient to employ a medical device. The device may be an implantable device, or an
	/// external assistive device, such as a walker.
	"""
	
	deviceUseStatement = "DeviceUseStatement"
	""" A record of a device being used by a patient where the record is the result of a report from the patient or
	/// another clinician.
	"""
	
	diagnosticReport = "DiagnosticReport"
	""" The findings and interpretation of diagnostic  tests performed on patients, groups of patients, devices, and
	/// locations, and/or specimens derived from these. The report includes clinical context such as requesting and
	/// provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted
	/// representation of diagnostic reports.
	"""
	
	documentManifest = "DocumentManifest"
	""" A collection of documents compiled for a purpose together with metadata that applies to the collection.
	"""
	
	documentReference = "DocumentReference"
	""" A reference to a document.
	"""
	
	domainResource = "DomainResource"
	""" A resource that includes narrative, extensions, and contained resources.
	"""
	
	effectEvidenceSynthesis = "EffectEvidenceSynthesis"
	""" The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a
	/// population where the effect estimate is derived from a combination of research studies.
	"""
	
	encounter = "Encounter"
	""" An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s)
	/// or assessing the health status of a patient.
	"""
	
	endpoint = "Endpoint"
	""" The technical details of an endpoint that can be used for electronic services, such as for web services
	/// providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
	"""
	
	enrollmentRequest = "EnrollmentRequest"
	""" This resource provides the insurance enrollment details to the insurer regarding a specified coverage.
	"""
	
	enrollmentResponse = "EnrollmentResponse"
	""" This resource provides enrollment and plan details from the processing of an Enrollment resource.
	"""
	
	episodeOfCare = "EpisodeOfCare"
	""" An association between a patient and an organization / healthcare provider(s) during which time encounters may
	/// occur. The managing organization assumes a level of responsibility for the patient during this time.
	"""
	
	eventDefinition = "EventDefinition"
	""" The EventDefinition resource provides a reusable description of when a particular event can occur.
	"""
	
	evidence = "Evidence"
	""" The Evidence resource describes the conditional state (population and any exposures being compared within the
	/// population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.
	"""
	
	evidenceVariable = "EvidenceVariable"
	""" The EvidenceVariable resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is
	/// about.
	"""
	
	exampleScenario = "ExampleScenario"
	""" Example of workflow instance.
	"""
	
	explanationOfBenefit = "ExplanationOfBenefit"
	""" This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally
	/// account balance information, for informing the subscriber of the benefits provided.
	"""
	
	familyMemberHistory = "FamilyMemberHistory"
	""" Significant health conditions for a person related to the patient relevant in the context of care for the
	/// patient.
	"""
	
	flag = "Flag"
	""" Prospective warnings of potential issues when providing care to the patient.
	"""
	
	goal = "Goal"
	""" Describes the intended objective(s) for a patient, group or organization care, for example, weight loss,
	/// restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement
	/// objective, etc.
	"""
	
	graphDefinition = "GraphDefinition"
	""" A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph
	/// by following references. The Graph Definition resource defines a set and makes rules about the set.
	"""
	
	group = "Group"
	""" Represents a defined collection of entities that may be discussed or acted upon collectively but which are not
	/// expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that
	/// isn't an Organization.
	"""
	
	guidanceResponse = "GuidanceResponse"
	""" A guidance response is the formal response to a guidance request, including any output parameters returned by
	/// the evaluation, as well as the description of any proposed actions to be taken.
	"""
	
	healthcareService = "HealthcareService"
	""" The details of a healthcare service available at a location.
	"""
	
	imagingStudy = "ImagingStudy"
	""" Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of
	/// which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or
	/// produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study
	/// may have multiple series of different modalities.
	"""
	
	immunization = "Immunization"
	""" Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a
	/// patient, a clinician or another party.
	"""
	
	immunizationEvaluation = "ImmunizationEvaluation"
	""" Describes a comparison of an immunization event against published recommendations to determine if the
	/// administration is "valid" in relation to those  recommendations.
	"""
	
	immunizationRecommendation = "ImmunizationRecommendation"
	""" A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with
	/// optional supporting justification.
	"""
	
	implementationGuide = "ImplementationGuide"
	""" A set of rules of how a particular interoperability or standards problem is solved - typically through the use
	/// of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole
	/// and to publish a computable definition of all the parts.
	"""
	
	insurancePlan = "InsurancePlan"
	""" Details of a Health Insurance product/plan provided by an organization.
	"""
	
	invoice = "Invoice"
	""" Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing
	/// purpose.
	"""
	
	itemInstance = "ItemInstance"
	""" A physical, countable instance of an item, for example one box or one unit.
	"""
	
	library = "Library"
	""" The Library resource is a general-purpose container for knowledge asset definitions. It can be used to describe
	/// and expose existing knowledge assets such as logic libraries and information model descriptions, as well as to
	/// describe a collection of knowledge assets.
	"""
	
	linkage = "Linkage"
	""" Identifies two or more records (resource instances) that are referring to the same real-world "occurrence".
	"""
	
	list = "List"
	""" A list is a curated collection of resources.
	"""
	
	location = "Location"
	""" Details and position information for a physical place where services are provided and resources and participants
	/// may be stored, found, contained, or accommodated.
	"""
	
	measure = "Measure"
	""" The Measure resource provides the definition of a quality measure.
	"""
	
	measureReport = "MeasureReport"
	""" The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to
	/// the resources involved in that calculation.
	"""
	
	media = "Media"
	""" A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided
	/// by direct reference.
	"""
	
	medication = "Medication"
	""" This resource is primarily used for the identification and definition of a medication for the purposes of
	/// prescribing, dispensing, and administering a medication as well as for making statements about medication use.
	"""
	
	medicationAdministration = "MedicationAdministration"
	""" Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple
	/// as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the
	/// authorizing prescription, and the specific encounter between patient and health care practitioner.
	"""
	
	medicationDispense = "MedicationDispense"
	""" Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a
	/// description of the medication product (supply) provided and the instructions for administering the medication.
	/// The medication dispense is the result of a pharmacy system responding to a medication order.
	"""
	
	medicationKnowledge = "MedicationKnowledge"
	""" Information about a medication that is used to support knowledge.
	"""
	
	medicationRequest = "MedicationRequest"
	""" An order or request for both supply of the medication and the instructions for administration of the medication
	/// to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or
	/// "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc.,
	/// and to harmonize with workflow patterns.
	"""
	
	medicationStatement = "MedicationStatement"
	""" A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the
	/// patient may be taking the medication now, or has taken the medication in the past or will be taking the
	/// medication in the future.  The source of this information can be the patient, significant other (such as a
	/// family member or spouse), or a clinician.  A common scenario where this information is captured is during the
	/// history taking process during a patient visit or stay.   The medication information may come from sources such
	/// as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or
	/// other party maintains.
	/// 
	/// The primary difference between a medication statement and a medication administration is that the medication
	/// administration has complete administration information and is based on actual administration information from
	/// the person who administered the medication.  A medication statement is often, if not always, less specific.
	/// There is no required date/time when the medication was administered, in fact we only know that a source has
	/// reported the patient is taking this medication, where details such as time, quantity, or rate or even medication
	/// product may be incomplete or missing or less precise.  As stated earlier, the medication statement information
	/// may come from the patient's memory, from a prescription bottle or from a list of medications the patient,
	/// clinician or other party maintains.  Medication administration is more formal and is not missing detailed
	/// information.
	"""
	
	medicinalProduct = "MedicinalProduct"
	""" Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory
	/// use).
	"""
	
	medicinalProductAuthorization = "MedicinalProductAuthorization"
	""" The regulatory authorization of a medicinal product.
	"""
	
	medicinalProductContraindication = "MedicinalProductContraindication"
	""" The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory
	/// purposes.
	"""
	
	medicinalProductIndication = "MedicinalProductIndication"
	""" Indication for the Medicinal Product.
	"""
	
	medicinalProductIngredient = "MedicinalProductIngredient"
	""" An ingredient of a manufactured item or pharmaceutical product.
	"""
	
	medicinalProductInteraction = "MedicinalProductInteraction"
	""" The interactions of the medicinal product with other medicinal products, or other forms of interactions.
	"""
	
	medicinalProductManufactured = "MedicinalProductManufactured"
	""" The manufactured item as contained in the packaged medicinal product.
	"""
	
	medicinalProductPackaged = "MedicinalProductPackaged"
	""" A medicinal product in a container or package.
	"""
	
	medicinalProductPharmaceutical = "MedicinalProductPharmaceutical"
	""" A pharmaceutical product described in terms of its composition and dose form.
	"""
	
	medicinalProductUndesirableEffect = "MedicinalProductUndesirableEffect"
	""" Describe the undesirable effects of the medicinal product.
	"""
	
	messageDefinition = "MessageDefinition"
	""" Defines the characteristics of a message that can be shared between systems, including the type of event that
	/// initiates the message, the content to be transmitted and what response(s), if any, are permitted.
	"""
	
	messageHeader = "MessageHeader"
	""" The header for a message exchange that is either requesting or responding to an action.  The reference(s) that
	/// are the subject of the action as well as other information related to the action are typically transmitted in a
	/// bundle in which the MessageHeader resource instance is the first resource in the bundle.
	"""
	
	molecularSequence = "MolecularSequence"
	""" Raw data describing a biological sequence.
	"""
	
	namingSystem = "NamingSystem"
	""" A curated namespace that issues unique symbols within that namespace for the identification of concepts, people,
	/// devices, etc.  Represents a "System" used within the Identifier and Coding data types.
	"""
	
	nutritionOrder = "NutritionOrder"
	""" A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
	"""
	
	observation = "Observation"
	""" Measurements and simple assertions made about a patient, device or other subject.
	"""
	
	observationDefinition = "ObservationDefinition"
	""" Set of definitional characteristics for a kind of observation or measurement produced or consumed by an
	/// orderable health care service.
	"""
	
	operationDefinition = "OperationDefinition"
	""" A formal computable definition of an operation (on the RESTful interface) or a named query (using the search
	/// interaction).
	"""
	
	operationOutcome = "OperationOutcome"
	""" A collection of error, warning, or information messages that result from a system action.
	"""
	
	organization = "Organization"
	""" A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some
	/// form of collective action.  Includes companies, institutions, corporations, departments, community groups,
	/// healthcare practice groups, payer/insurer, etc.
	"""
	
	organizationAffiliation = "OrganizationAffiliation"
	""" Defines an affiliation/assotiation/relationship between 2 distinct oganizations, that is not a part-of
	/// relationship/sub-division relationship.
	"""
	
	parameters = "Parameters"
	""" This resource is a non-persisted resource used to pass information into and back from an
	/// [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
	"""
	
	patient = "Patient"
	""" Demographics and other administrative information about an individual or animal receiving care or other health-
	/// related services.
	"""
	
	paymentNotice = "PaymentNotice"
	""" This resource provides the status of the payment for goods and services rendered, and the request and response
	/// resource references.
	"""
	
	paymentReconciliation = "PaymentReconciliation"
	""" This resource provides payment details and claim references supporting a bulk payment.
	"""
	
	person = "Person"
	""" Demographics and administrative information about a person independent of a specific health-related context.
	"""
	
	planDefinition = "PlanDefinition"
	""" This resource allows for the definition of various types of plans as a sharable, consumable, and executable
	/// artifact. The resource is general enough to support the description of a broad range of clinical artifacts such
	/// as clinical decision support rules, order sets and protocols.
	"""
	
	practitioner = "Practitioner"
	""" A person who is directly or indirectly involved in the provisioning of healthcare.
	"""
	
	practitionerRole = "PractitionerRole"
	""" A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a
	/// period of time.
	"""
	
	procedure = "Procedure"
	""" An action that is or was performed on or for a patient. This can be a physical intervention like an operation,
	/// or less invasive like long term services, counseling, or hypnotherapy.
	"""
	
	processRequest = "ProcessRequest"
	""" This resource provides the target, request and response, and action details for an action to be performed by the
	/// target on or about existing resources.
	"""
	
	processResponse = "ProcessResponse"
	""" This resource provides processing status, errors and notes from the processing of a resource.
	"""
	
	provenance = "Provenance"
	""" Provenance of a resource is a record that describes entities and processes involved in producing and delivering
	/// or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity,
	/// enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can
	/// themselves become important records with their own provenance. Provenance statement indicates clinical
	/// significance in terms of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in
	/// lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact
	/// security, privacy, and trust policies.
	"""
	
	questionnaire = "Questionnaire"
	""" A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide
	/// detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data
	/// collection.
	"""
	
	questionnaireResponse = "QuestionnaireResponse"
	""" A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets,
	/// corresponding to the structure of the grouping of the questionnaire being responded to.
	"""
	
	relatedPerson = "RelatedPerson"
	""" Information about a person that is involved in the care for a patient, but who is not the target of healthcare,
	/// nor has a formal responsibility in the care process.
	"""
	
	requestGroup = "RequestGroup"
	""" A group of related requests that can be used to capture intended activities that have inter-dependencies such as
	/// "give this medication after that one".
	"""
	
	researchDefinition = "ResearchDefinition"
	""" The ResearchDefinition resource describes the conditional state (population and any exposures being compared
	/// within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is
	/// about.
	"""
	
	researchElementDefinition = "ResearchElementDefinition"
	""" The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion,
	/// recommendation) is about.
	"""
	
	researchStudy = "ResearchStudy"
	""" A process where a researcher or organization plans and then executes a series of steps intended to increase the
	/// field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and
	/// other information about medications, devices, therapies and other interventional and investigative techniques.
	/// A ResearchStudy involves the gathering of information about human or animal subjects.
	"""
	
	researchSubject = "ResearchSubject"
	""" A physical entity which is the primary unit of operational and/or administrative interest in a study.
	"""
	
	resource = "Resource"
	""" This is the base resource type for everything.
	"""
	
	riskAssessment = "RiskAssessment"
	""" An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
	"""
	
	riskEvidenceSynthesis = "RiskEvidenceSynthesis"
	""" The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state
	/// where the risk estimate is derived from a combination of research studies.
	"""
	
	schedule = "Schedule"
	""" A container for slots of time that may be available for booking appointments.
	"""
	
	searchParameter = "SearchParameter"
	""" A search parameter that defines a named search item that can be used to search/filter on a resource.
	"""
	
	serviceRequest = "ServiceRequest"
	""" A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
	"""
	
	slot = "Slot"
	""" A slot of time on a schedule that may be available for booking appointments.
	"""
	
	specimen = "Specimen"
	""" A sample to be used for analysis.
	"""
	
	specimenDefinition = "SpecimenDefinition"
	""" A kind of specimen with associated set of requirements.
	"""
	
	structureDefinition = "StructureDefinition"
	""" A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined
	/// in FHIR, and also for describing extensions and constraints on resources and data types.
	"""
	
	structureMap = "StructureMap"
	""" A Map of relationships between 2 structures that can be used to transform data.
	"""
	
	subscription = "Subscription"
	""" The subscription resource is used to define a push-based subscription from a server to another system. Once a
	/// subscription is registered with the server, the server checks every resource that is created or updated, and if
	/// the resource matches the given criteria, it sends a message on the defined "channel" so that another system can
	/// take an appropriate action.
	"""
	
	substance = "Substance"
	""" A homogeneous material with a definite composition.
	"""
	
	substanceNucleicAcid = "SubstanceNucleicAcid"
	""" Nucleic acids are defined by three distinct elements: the base, sugar and linkage. Individual substance/moiety
	/// IDs will be created for each of these elements. The nucleotide sequence will be always entered in the 5’-3’
	/// direction.
	"""
	
	substancePolymer = "SubstancePolymer"
	""" Todo.
	"""
	
	substanceProtein = "SubstanceProtein"
	""" A SubstanceProtein is defined as a single unit of a linear amino acid sequence, or a combination of subunits
	/// that are either covalently linked or have a defined invariant stoichiometric relationship. This includes all
	/// synthetic, recombinant and purified SubstanceProteins of defined sequence, whether the use is therapeutic or
	/// prophylactic. This set of elements will be used to describe albumins, coagulation factors, cytokines, growth
	/// factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant vaccines, and
	/// immunomodulators.
	"""
	
	substanceReferenceInformation = "SubstanceReferenceInformation"
	""" Todo.
	"""
	
	substanceSourceMaterial = "SubstanceSourceMaterial"
	""" Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a
	/// material that can result in or can be modified to form a substance. This set of data elements shall be used to
	/// define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described
	/// using a controlled vocabulary as required. This information is captured for naturally derived polymers ( .
	/// starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level
	/// defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For
	/// Herbal preparations, the fraction information will be captured at the Substance information level and additional
	/// information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for
	/// further explanation the Substance Class: Structurally Diverse and the herbal annex.
	"""
	
	substanceSpecification = "SubstanceSpecification"
	""" The detailed description of a substance, typically at a level beyond what is used for prescribing.
	"""
	
	supplyDelivery = "SupplyDelivery"
	""" Record of delivery of what is supplied.
	"""
	
	supplyRequest = "SupplyRequest"
	""" A record of a request for a medication, substance or device used in the healthcare setting.
	"""
	
	task = "Task"
	""" A task to be performed.
	"""
	
	terminologyCapabilities = "TerminologyCapabilities"
	""" A Terminology Capabilities documents a set of capabilities (behaviors) of a FHIR Server that may be used as a
	/// statement of actual server functionality or a statement of required or desired server implementation.
	"""
	
	testReport = "TestReport"
	""" A summary of information based on the results of executing a TestScript.
	"""
	
	testScript = "TestScript"
	""" A structured set of tests against a FHIR server or client implementation to determine compliance against the
	/// FHIR specification.
	"""
	
	valueSet = "ValueSet"
	""" A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a
	/// particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded
	/// elements](terminologies.html).
	"""
	
	verificationResult = "VerificationResult"
	""" Describes validation requirements, source(s), status and dates for one or more elements.
	"""
	
	visionPrescription = "VisionPrescription"
	""" An authorization for the provision of glasses and/or contact lenses to a patient.
	"""
}


class ResourceValidationMode(object) {
	""" Codes indicating the type of validation to perform.

	URL: http://hl7.org/fhir/resource-validation-mode
	ValueSet: http://hl7.org/fhir/ValueSet/resource-validation-mode
	"""
	
	create = "create"
	""" The server checks the content, and then checks that the content would be acceptable as a create (e.g. that the
	/// content would not violate any uniqueness constraints).
	"""
	
	update = "update"
	""" The server checks the content, and then checks that it would accept it as an update against the nominated
	/// specific resource (e.g. that there are no changes to immutable fields the server does not allow to change and
	/// checking version integrity if appropriate).
	"""
	
	delete = "delete"
	""" The server ignores the content and checks that the nominated resource is allowed to be deleted (e.g. checking
	/// referential integrity rules).
	"""
	
	profile = "profile"
	""" The server checks an existing resource (must be nominated by id, not provided as a parameter) as valid against
	/// the nominated profile.
	"""
}


class ResourceVersionPolicy(object) {
	""" How the system supports versioning for a resource.

	URL: http://hl7.org/fhir/versioning-policy
	ValueSet: http://hl7.org/fhir/ValueSet/versioning-policy
	"""
	
	noVersion = "no-version"
	""" VersionId meta-property is not supported (server) or used (client).
	"""
	
	versioned = "versioned"
	""" VersionId meta-property is supported (server) or used (client).
	"""
	
	versionedUpdate = "versioned-update"
	""" VersionId must be correct for updates (server) or will be specified (If-match header) for updates (client).
	"""
}


class ResponseType(object) {
	""" The kind of response to a message.

	URL: http://hl7.org/fhir/response-code
	ValueSet: http://hl7.org/fhir/ValueSet/response-code
	"""
	
	ok = "ok"
	""" The message was accepted and processed without error.
	"""
	
	transientError = "transient-error"
	""" Some internal unexpected error occurred - wait and try again. Note - this is usually used for things like
	/// database unavailable, which may be expected to resolve, though human intervention may be required.
	"""
	
	fatalError = "fatal-error"
	""" The message was rejected because of a problem with the content. There is no point in re-sending without change.
	/// The response narrative SHALL describe the issue.
	"""
}


class RestfulCapabilityMode(object) {
	""" The mode of a RESTful capability statement.

	URL: http://hl7.org/fhir/restful-capability-mode
	ValueSet: http://hl7.org/fhir/ValueSet/restful-capability-mode
	"""
	
	client = "client"
	""" The application acts as a client for this resource.
	"""
	
	server = "server"
	""" The application acts as a server for this resource.
	"""
}


class RestfulSecurityService(object) {
	""" Types of security services used with FHIR.

	URL: http://terminology.hl7.org/CodeSystem/restful-security-service
	ValueSet: http://hl7.org/fhir/ValueSet/restful-security-service
	"""
	
	oAuth = "OAuth"
	""" OAuth (unspecified version see oauth.net).
	"""
	
	sMARTOnFHIR = "SMART-on-FHIR"
	""" OAuth2 using SMART-on-FHIR profile (see http://docs.smarthealthit.org/).
	"""
	
	NTLM = "NTLM"
	""" Microsoft NTLM Authentication.
	"""
	
	basic = "Basic"
	""" Basic authentication defined in HTTP specification.
	"""
	
	kerberos = "Kerberos"
	""" see http://www.ietf.org/rfc/rfc4120.txt.
	"""
	
	certificates = "Certificates"
	""" SSL where client must have a certificate registered with the server.
	"""
}


class RiskEstimateType(object) {
	""" Whether the risk estimate is dichotomous, continuous or qualitative and the specific type of risk estimate (eg
proportion or median).

	URL: http://terminology.hl7.org/CodeSystem/risk-estimate-type
	ValueSet: http://hl7.org/fhir/ValueSet/risk-estimate-type
	"""
	
	proportion = "proportion"
	""" dichotomous measure (present or absent) reported as a ratio compared to the denominator of 1 (A percentage is a
	/// proportion with denominator of 100).
	"""
	
	derivedProportion = "derivedProportion"
	""" A special use case where the proportion is derived from a formula rather than derived from summary evidence.
	"""
	
	mean = "mean"
	""" continuous numerical measure reported as an average.
	"""
	
	median = "median"
	""" continuous numerical measure reported as the middle of the range.
	"""
	
	count = "count"
	""" descriptive measure reported as total number of items.
	"""
	
	descriptive = "descriptive"
	""" descriptive measure reported as narrative.
	"""
}


class SearchComparator(object) {
	""" What Search Comparator Codes are supported in search.

	URL: http://hl7.org/fhir/search-comparator
	ValueSet: http://hl7.org/fhir/ValueSet/search-comparator
	"""
	
	eq = "eq"
	""" the value for the parameter in the resource is equal to the provided value.
	"""
	
	ne = "ne"
	""" the value for the parameter in the resource is not equal to the provided value.
	"""
	
	gt = "gt"
	""" the value for the parameter in the resource is greater than the provided value.
	"""
	
	lt = "lt"
	""" the value for the parameter in the resource is less than the provided value.
	"""
	
	ge = "ge"
	""" the value for the parameter in the resource is greater or equal to the provided value.
	"""
	
	le = "le"
	""" the value for the parameter in the resource is less or equal to the provided value.
	"""
	
	sa = "sa"
	""" the value for the parameter in the resource starts after the provided value.
	"""
	
	eb = "eb"
	""" the value for the parameter in the resource ends before the provided value.
	"""
	
	ap = "ap"
	""" the value for the parameter in the resource is approximately the same to the provided value.
	"""
}


class SearchEntryMode(object) {
	""" Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey
information or warning information about the search process.

	URL: http://hl7.org/fhir/search-entry-mode
	ValueSet: http://hl7.org/fhir/ValueSet/search-entry-mode
	"""
	
	match = "match"
	""" This resource matched the search specification.
	"""
	
	include = "include"
	""" This resource is returned because it is referred to from another resource in the search set.
	"""
	
	outcome = "outcome"
	""" An OperationOutcome that provides additional information about the processing of a search.
	"""
}


class SearchModifierCode(object) {
	""" A supported modifier for a search parameter.

	URL: http://hl7.org/fhir/search-modifier-code
	ValueSet: http://hl7.org/fhir/ValueSet/search-modifier-code
	"""
	
	missing = "missing"
	""" The search parameter returns resources that have a value or not.
	"""
	
	exact = "exact"
	""" The search parameter returns resources that have a value that exactly matches the supplied parameter (the whole
	/// string, including casing and accents).
	"""
	
	contains = "contains"
	""" The search parameter returns resources that include the supplied parameter value anywhere within the field being
	/// searched.
	"""
	
	not = "not"
	""" The search parameter returns resources that do not contain a match.
	"""
	
	text = "text"
	""" The search parameter is processed as a string that searches text associated with the code/value - either
	/// CodeableConcept.text, Coding.display, or Identifier.type.text.
	"""
	
	in = "in"
	""" The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests
	/// whether the coding is in the specified value set.
	"""
	
	notIn = "not-in"
	""" The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests
	/// whether the coding is not in the specified value set.
	"""
	
	below = "below"
	""" The search parameter tests whether the value in a resource is subsumed by the specified value (is-a, or
	/// hierarchical relationships).
	"""
	
	above = "above"
	""" The search parameter tests whether the value in a resource subsumes the specified value (is-a, or hierarchical
	/// relationships).
	"""
	
	type = "type"
	""" The search parameter only applies to the Resource Type specified as a modifier (e.g. the modifier is not
	/// actually :type, but :Patient etc.).
	"""
	
	identifier = "identifier"
	""" The search parameter applies to the identifier on the resource, not the reference.
	"""
	
	ofType = "ofType"
	""" The search parameter has the format system|code|value, where the system and code refer to an
	/// Identifier.type.coding.system and .code, and match if any of the type codes match. All 3 parts must be present.
	"""
}


class SearchParamType(object) {
	""" Data types allowed to be used for search parameters.

	URL: http://hl7.org/fhir/search-param-type
	ValueSet: http://hl7.org/fhir/ValueSet/search-param-type
	"""
	
	number = "number"
	""" Search parameter SHALL be a number (a whole number, or a decimal).
	"""
	
	date = "date"
	""" Search parameter is on a date/time. The date format is the standard XML format, though other formats may be
	/// supported.
	"""
	
	string = "string"
	""" Search parameter is a simple string, like a name part. Search is case-insensitive and accent-insensitive. May
	/// match just the start of a string. String parameters may contain spaces.
	"""
	
	token = "token"
	""" Search parameter on a coded element or identifier. May be used to search through the text, display, code and
	/// code/codesystem (for codes) and label, system and key (for identifier). Its value is either a string or a pair
	/// of namespace and value, separated by a "|", depending on the modifier used.
	"""
	
	reference = "reference"
	""" A reference to another resource (Reference or canonical).
	"""
	
	composite = "composite"
	""" A composite search parameter that combines a search on two values together.
	"""
	
	quantity = "quantity"
	""" A search parameter that searches on a quantity.
	"""
	
	uri = "uri"
	""" A search parameter that searches on a URI (RFC 3986).
	"""
	
	special = "special"
	""" Special logic applies to this parameter per the description of the search parameter.
	"""
}


class SequenceStatus(object) {
	""" Codes providing the status of the variant test result.

	URL: http://terminology.hl7.org/CodeSystem/variant-state
	ValueSet: http://hl7.org/fhir/ValueSet/variant-state
	"""
	
	positive = "positive"
	""" the variant is detected.
	"""
	
	negative = "negative"
	""" no variant is detected.
	"""
	
	absent = "absent"
	""" result of the variant is missing.
	"""
}


class SequenceType(object) {
	""" Type if a sequence -- DNA, RNA, or amino acid sequence.

	URL: http://hl7.org/fhir/sequence-type
	ValueSet: http://hl7.org/fhir/ValueSet/sequence-type
	"""
	
	aa = "aa"
	""" Amino acid sequence.
	"""
	
	dna = "dna"
	""" DNA Sequence.
	"""
	
	rna = "rna"
	""" RNA Sequence.
	"""
}


class ServiceProvisionConditions(object) {
	""" The code(s) that detail the conditions under which the healthcare service is available/offered.

	URL: http://terminology.hl7.org/CodeSystem/service-provision-conditions
	ValueSet: http://hl7.org/fhir/ValueSet/service-provision-conditions
	"""
	
	free = "free"
	""" This service is available for no patient cost.
	"""
	
	disc = "disc"
	""" There are discounts available on this service for qualifying patients.
	"""
	
	cost = "cost"
	""" Fees apply for this service.
	"""
}


class SlicingRules(object) {
	""" How slices are interpreted when evaluating an instance.

	URL: http://hl7.org/fhir/resource-slicing-rules
	ValueSet: http://hl7.org/fhir/ValueSet/resource-slicing-rules
	"""
	
	closed = "closed"
	""" No additional content is allowed other than that described by the slices in this profile.
	"""
	
	open = "open"
	""" Additional content is allowed anywhere in the list.
	"""
	
	openAtEnd = "openAtEnd"
	""" Additional content is allowed, but only at the end of the list. Note that using this requires that the slices be
	/// ordered, which makes it hard to share uses. This should only be done where absolutely required.
	"""
}


class SlotStatus(object) {
	""" The free/busy status of the slot.

	URL: http://hl7.org/fhir/slotstatus
	ValueSet: http://hl7.org/fhir/ValueSet/slotstatus
	"""
	
	busy = "busy"
	""" Indicates that the time interval is busy because one  or more events have been scheduled for that interval.
	"""
	
	free = "free"
	""" Indicates that the time interval is free for scheduling.
	"""
	
	busyUnavailable = "busy-unavailable"
	""" Indicates that the time interval is busy and that the interval cannot be scheduled.
	"""
	
	busyTentative = "busy-tentative"
	""" Indicates that the time interval is busy because one or more events have been tentatively scheduled for that
	/// interval.
	"""
	
	enteredInError = "entered-in-error"
	""" This instance should not have been part of this patient's medical record.
	"""
}


class SmartCapabilities(object) {
	""" Codes that define what the server is capable of.

	URL: http://terminology.hl7.org/CodeSystem/smart-capabilities
	ValueSet: http://hl7.org/fhir/ValueSet/smart-capabilities
	"""
	
	launchEhr = "launch-ehr"
	""" support for SMART’s EHR Launch mode.
	"""
	
	launchStandalone = "launch-standalone"
	""" support for SMART’s Standalone Launch mode.
	"""
	
	clientPublic = "client-public"
	""" support for SMART’s public client profile (no client authentication).
	"""
	
	clientConfidentialSymmetric = "client-confidential-symmetric"
	""" support for SMART’s confidential client profile (symmetric client secret authentication).
	"""
	
	ssoOpenidConnect = "sso-openid-connect"
	""" support for SMART’s OpenID Connect profile.
	"""
	
	contextPassthroughBanner = "context-passthrough-banner"
	""" support for “need patient banner” launch context (conveyed via need_patient_banner token parameter).
	"""
	
	contextPassthroughStyle = "context-passthrough-style"
	""" support for “SMART style URL” launch context (conveyed via smart_style_url token parameter).
	"""
	
	contextEhrPatient = "context-ehr-patient"
	""" support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter).
	"""
	
	contextEhrEncounter = "context-ehr-encounter"
	""" support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter).
	"""
	
	contextStandalonePatient = "context-standalone-patient"
	""" support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter).
	"""
	
	contextStandaloneEncounter = "context-standalone-encounter"
	""" support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter).
	"""
	
	permissionOffline = "permission-offline"
	""" support for refresh tokens (requested by offline_access scope).
	"""
	
	permissionPatient = "permission-patient"
	""" support for patient-level scopes (e.g. patient/Observation.read).
	"""
	
	permissionUser = "permission-user"
	""" support for user-level scopes (e.g. user/Appointment.read).
	"""
}


class SortDirection(object) {
	""" The possible sort directions, ascending or descending.

	URL: http://hl7.org/fhir/sort-direction
	ValueSet: http://hl7.org/fhir/ValueSet/sort-direction
	"""
	
	ascending = "ascending"
	""" Sort by the value ascending, so that lower values appear first.
	"""
	
	descending = "descending"
	""" Sort by the value descending, so that lower values appear last.
	"""
}


class SpecialValues(object) {
	""" A set of generally useful codes defined so they can be included in value sets.

	URL: http://terminology.hl7.org/CodeSystem/special-values
	ValueSet: http://hl7.org/fhir/ValueSet/special-values
	"""
	
	true = "true"
	""" Boolean true.
	"""
	
	false = "false"
	""" Boolean false.
	"""
	
	trace = "trace"
	""" The content is greater than zero, but too small to be quantified.
	"""
	
	sufficient = "sufficient"
	""" The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the
	/// bulk of the material.
	"""
	
	withdrawn = "withdrawn"
	""" The value is no longer available.
	"""
	
	nilKnown = "nil-known"
	""" The are no known applicable values in this context.
	"""
}


class SpecimenContainedPreference(object) {
	""" Degree of preference of a type of conditioned specimen.

	URL: http://hl7.org/fhir/specimen-contained-preference
	ValueSet: http://hl7.org/fhir/ValueSet/specimen-contained-preference
	"""
	
	preferred = "preferred"
	""" This type of contained specimen is preferred to collect this kind of specimen.
	"""
	
	alternate = "alternate"
	""" This type of conditioned specimen is an alternate.
	"""
}


class SpecimenStatus(object) {
	""" Codes providing the status/availability of a specimen.

	URL: http://hl7.org/fhir/specimen-status
	ValueSet: http://hl7.org/fhir/ValueSet/specimen-status
	"""
	
	available = "available"
	""" The physical specimen is present and in good condition.
	"""
	
	unavailable = "unavailable"
	""" There is no physical specimen because it is either lost, destroyed or consumed.
	"""
	
	unsatisfactory = "unsatisfactory"
	""" The specimen cannot be used because of a quality issue such as a broken container, contamination, or too old.
	"""
	
	enteredInError = "entered-in-error"
	""" The specimen was entered in error and therefore nullified.
	"""
}


class StandardsStatus(object) {
	""" HL7 Ballot/Standards status of artifact.

	URL: http://terminology.hl7.org/CodeSystem/standards-status
	ValueSet: http://hl7.org/fhir/ValueSet/standards-status
	"""
	
	draft = "draft"
	""" This portion of the specification is not considered to be complete enough or sufficiently reviewed to be safe
	/// for implementation. It may have known issues or still be in the "in development" stage. It is included in the
	/// publication as a place-holder, to solicit feedback from the implementation community and/or to give implementers
	/// some insight as to functionality likely to be included in future versions of the specification. Content at this
	/// level should only be implemented by the brave or desperate and is very much "use at your own risk". The content
	/// that is Draft that will usually be elevated to Trial Use once review and correction is complete after it has
	/// been subjected to ballot.
	"""
	
	normative = "normative"
	""" This content has been subject to review and production implementation in a wide variety of environments. The
	/// content is considered to be stable and has been 'locked', subjecting it to FHIR Inter-version Compatibility
	/// Rules. While changes are possible, they are expected to be infrequent and are tightly constrained. Compatibility
	/// Rules.
	"""
	
	trialUse = "trial-use"
	""" This content has been well reviewed and is considered by the authors to be ready for use in production systems.
	/// It has been subjected to ballot and approved as an official standard. However, it has not yet seen widespread
	/// use in production across the full spectrum of environments it is intended to be used in. In some cases, there
	/// may be documented known issues that require implementation experience to determine appropriate resolutions for.
	/// 
	/// Future versions of FHIR may make significant changes to Trial Use content that are not compatible with
	/// previously published content.
	"""
	
	informative = "informative"
	""" This portion of the specification is provided for implementer assistance, and does not make rules that
	/// implementers are required to follow. Typical examples of this content in the FHIR specification are tables of
	/// contents, registries, examples, and implementer advice.
	"""
	
	deprecated = "deprecated"
	""" This portion of the specification is provided for implementer assistance, and does not make rules that
	/// implementers are required to follow. Typical examples of this content in the FHIR specification are tables of
	/// contents, registries, examples, and implementer advice.
	"""
	
	external = "external"
	""" This is content that is managed outside the FHIR Specification, but included for implementer convenience.
	"""
}


class StrandType(object) {
	""" Type for strand.

	URL: http://hl7.org/fhir/strand-type
	ValueSet: http://hl7.org/fhir/ValueSet/strand-type
	"""
	
	watson = "watson"
	""" Watson strand of reference sequence.
	"""
	
	crick = "crick"
	""" Crick strand of reference sequence.
	"""
}


class StrengthOfRecommendationRating(object) {
	""" A rating system that describes the strength of the recommendation, such as the GRADE, DynaMed, or HGPS systems.

	URL: http://terminology.hl7.org/CodeSystem/recommendation-strength
	ValueSet: http://hl7.org/fhir/ValueSet/recommendation-strength
	"""
	
	strong = "strong"
	""" Strong recommendation.
	"""
	
	weak = "weak"
	""" Weak recommendation.
	"""
}


class StructureDefinitionKind(object) {
	""" Defines the type of structure that a definition is describing.

	URL: http://hl7.org/fhir/structure-definition-kind
	ValueSet: http://hl7.org/fhir/ValueSet/structure-definition-kind
	"""
	
	primitiveType = "primitive-type"
	""" A primitive type that has a value and an extension. These can be used throughout complex datatype, Resource and
	/// extension definitions. Only the base specification can define primitive types.
	"""
	
	complexType = "complex-type"
	""" A  complex structure that defines a set of data elements that is suitable for use in 'resources'. The base
	/// specification defines a number of complex types, and other specifications can define additional types. These
	/// structures do not have a maintained identity.
	"""
	
	resource = "resource"
	""" A 'resource' - a directed acyclic graph of elements that aggregrates other types into an identifiable entity.
	/// The base FHIR resources are defined by the FHIR specification itself but other 'resources' can be defined in
	/// additional specifications (though these will not be recognised as 'resources' by the FHIR specification (i.e.
	/// they do not get end-points etc, or act as the targets of references in FHIR defined resources - though other
	/// specificatiosn can treat them this way).
	"""
	
	logical = "logical"
	""" A pattern or a template that is not intended to be a real resource or complex type.
	"""
}


class StructureMapContextType(object) {
	""" How to interpret the context.

	URL: http://hl7.org/fhir/map-context-type
	ValueSet: http://hl7.org/fhir/ValueSet/map-context-type
	"""
	
	type = "type"
	""" The context specifies a type.
	"""
	
	variable = "variable"
	""" The context specifies a variable.
	"""
}


class StructureMapGroupTypeMode(object) {
	""" If this is the default rule set to apply for the source type, or this combination of types.

	URL: http://hl7.org/fhir/map-group-type-mode
	ValueSet: http://hl7.org/fhir/ValueSet/map-group-type-mode
	"""
	
	none = "none"
	""" This group is not a default group for the types.
	"""
	
	types = "types"
	""" This group is a default mapping group for the specified types and for the primary source type.
	"""
	
	typeAndTypes = "type-and-types"
	""" This group is a default mapping group for the specified types.
	"""
}


class StructureMapInputMode(object) {
	""" Mode for this instance of data.

	URL: http://hl7.org/fhir/map-input-mode
	ValueSet: http://hl7.org/fhir/ValueSet/map-input-mode
	"""
	
	source = "source"
	""" Names an input instance used a source for mapping.
	"""
	
	target = "target"
	""" Names an instance that is being populated.
	"""
}


class StructureMapModelMode(object) {
	""" How the referenced structure is used in this mapping.

	URL: http://hl7.org/fhir/map-model-mode
	ValueSet: http://hl7.org/fhir/ValueSet/map-model-mode
	"""
	
	source = "source"
	""" This structure describes an instance passed to the mapping engine that is used a source of data.
	"""
	
	queried = "queried"
	""" This structure describes an instance that the mapping engine may ask for that is used a source of data.
	"""
	
	target = "target"
	""" This structure describes an instance passed to the mapping engine that is used a target of data.
	"""
	
	produced = "produced"
	""" This structure describes an instance that the mapping engine may ask to create that is used a target of data.
	"""
}


class StructureMapSourceListMode(object) {
	""" If field is a list, how to manage the source.

	URL: http://hl7.org/fhir/map-source-list-mode
	ValueSet: http://hl7.org/fhir/ValueSet/map-source-list-mode
	"""
	
	first = "first"
	""" Only process this rule for the first in the list.
	"""
	
	not_first = "not_first"
	""" Process this rule for all but the first.
	"""
	
	last = "last"
	""" Only process this rule for the last in the list.
	"""
	
	not_last = "not_last"
	""" Process this rule for all but the last.
	"""
	
	only_one = "only_one"
	""" Only process this rule is there is only item.
	"""
}


class StructureMapTargetListMode(object) {
	""" If field is a list, how to manage the production.

	URL: http://hl7.org/fhir/map-target-list-mode
	ValueSet: http://hl7.org/fhir/ValueSet/map-target-list-mode
	"""
	
	first = "first"
	""" when the target list is being assembled, the items for this rule go first. If more than one rule defines a first
	/// item (for a given instance of mapping) then this is an error.
	"""
	
	share = "share"
	""" the target instance is shared with the target instances generated by another rule (up to the first common n
	/// items, then create new ones).
	"""
	
	last = "last"
	""" when the target list is being assembled, the items for this rule go last. If more than one rule defines a last
	/// item (for a given instance of mapping) then this is an error.
	"""
	
	collate = "collate"
	""" re-use the first item in the list, and keep adding content to it.
	"""
}


class StructureMapTransform(object) {
	""" How data is copied/created.

	URL: http://hl7.org/fhir/map-transform
	ValueSet: http://hl7.org/fhir/ValueSet/map-transform
	"""
	
	create = "create"
	""" create(type : string) - type is passed through to the application on the standard API, and must be known by it.
	"""
	
	copy = "copy"
	""" copy(source).
	"""
	
	truncate = "truncate"
	""" truncate(source, length) - source must be stringy type.
	"""
	
	escape = "escape"
	""" escape(source, fmt1, fmt2) - change source from one kind of escaping to another (plain, java, xml, json). note
	/// that this is for when the string itself is escaped.
	"""
	
	cast = "cast"
	""" cast(source, type?) - case source from one type to another. target type can be left as implicit if there is one
	/// and only one target type known.
	"""
	
	append = "append"
	""" append(source...) - source is element or string.
	"""
	
	translate = "translate"
	""" translate(source, uri_of_map) - use the translate operation.
	"""
	
	reference = "reference"
	""" reference(source : object) - return a string that references the provided tree properly.
	"""
	
	dateOp = "dateOp"
	""" Perform a date operation. *Parameters to be documented*.
	"""
	
	uuid = "uuid"
	""" Generate a random UUID (in lowercase). No Parameters.
	"""
	
	pointer = "pointer"
	""" Return the appropriate string to put in a reference that refers to the resource provided as a parameter.
	"""
	
	evaluate = "evaluate"
	""" Execute the supplied FHIRPath expression and use the value returned by that.
	"""
	
	cc = "cc"
	""" Create a CodeableConcept. Parameters = (text) or (system. Code[, display]).
	"""
	
	C = "c"
	""" Create a Coding. Parameters = (system. Code[, display]).
	"""
	
	qty = "qty"
	""" Create a quantity. Parameters = (text) or (value, unit, [system, code]) where text is the natural representation
	/// e.g. [comparator]value[space]unit.
	"""
	
	id = "id"
	""" Create an identifier. Parameters = (system, value[, type]) where type is a code from the identifier type value
	/// set.
	"""
	
	cp = "cp"
	""" Create a contact details. Parameters = (value) or (system, value). If no system is provided, the system should
	/// be inferred from the content of the value.
	"""
}


class StudyType(object) {
	""" Types of research studies (types of research methods).

	URL: http://terminology.hl7.org/CodeSystem/study-type
	ValueSet: http://hl7.org/fhir/ValueSet/study-type
	"""
	
	RCT = "RCT"
	""" randomized controlled trial.
	"""
	
	CCT = "CCT"
	""" controlled (but not randomized) trial.
	"""
	
	cohort = "cohort"
	""" observational study comparing cohorts.
	"""
	
	caseControl = "case-control"
	""" case-control study.
	"""
	
	series = "series"
	""" uncontrolled cohort or case series.
	"""
	
	caseReport = "case-report"
	""" a single case report.
	"""
	
	mixed = "mixed"
	""" a combination of 1 or more types of studies.
	"""
}


class SubscriptionChannelType(object) {
	""" The type of method used to execute a subscription.

	URL: http://hl7.org/fhir/subscription-channel-type
	ValueSet: http://hl7.org/fhir/ValueSet/subscription-channel-type
	"""
	
	restHook = "rest-hook"
	""" The channel is executed by making a post to the URI. If a payload is included, the URL is interpreted as the
	/// service base, and an update (PUT) is made.
	"""
	
	websocket = "websocket"
	""" The channel is executed by sending a packet across a web socket connection maintained by the client. The URL
	/// identifies the websocket, and the client binds to this URL.
	"""
	
	email = "email"
	""" The channel is executed by sending an email to the email addressed in the URI (which must be a mailto:).
	"""
	
	sms = "sms"
	""" The channel is executed by sending an SMS message to the phone number identified in the URL (tel:).
	"""
	
	message = "message"
	""" The channel is executed by sending a message (e.g. a Bundle with a MessageHeader resource etc.) to the
	/// application identified in the URI.
	"""
}


class SubscriptionStatus(object) {
	""" The status of a subscription.

	URL: http://hl7.org/fhir/subscription-status
	ValueSet: http://hl7.org/fhir/ValueSet/subscription-status
	"""
	
	requested = "requested"
	""" The client has requested the subscription, and the server has not yet set it up.
	"""
	
	active = "active"
	""" The subscription is active.
	"""
	
	error = "error"
	""" The server has an error executing the notification.
	"""
	
	off = "off"
	""" Too many errors have occurred or the subscription has expired.
	"""
}


class SubscriptionTag(object) {
	""" Tags to put on a resource after subscriptions have been sent.

	URL: http://terminology.hl7.org/CodeSystem/subscription-tag
	ValueSet: http://hl7.org/fhir/ValueSet/subscription-tag
	"""
	
	queued = "queued"
	""" The message has been queued for processing on a destination systems.
	"""
	
	delivered = "delivered"
	""" The message has been delivered to its intended recipient.
	"""
}


class SupplyDeliveryStatus(object) {
	""" Status of the supply delivery.

	URL: http://hl7.org/fhir/supplydelivery-status
	ValueSet: http://hl7.org/fhir/ValueSet/supplydelivery-status
	"""
	
	inProgress = "in-progress"
	""" Supply has been requested, but not delivered.
	"""
	
	completed = "completed"
	""" Supply has been delivered ("completed").
	"""
	
	abandoned = "abandoned"
	""" Delivery was not completed.
	"""
	
	enteredInError = "entered-in-error"
	""" This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
	"""
}


class SupplyRequestReason(object) {
	""" The reason why the supply item was requested.

	URL: http://terminology.hl7.org/CodeSystem/supplyrequest-reason
	ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-reason
	"""
	
	patientCare = "patient-care"
	""" The supply has been requested for use in direct patient care.
	"""
	
	wardStock = "ward-stock"
	""" The supply has been requested for creating or replenishing ward stock.
	"""
}


class SupplyRequestStatus(object) {
	""" Status of the supply request.

	URL: http://hl7.org/fhir/supplyrequest-status
	ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-status
	"""
	
	draft = "draft"
	""" The request has been created but is not yet complete or ready for action.
	"""
	
	active = "active"
	""" The request is ready to be acted upon.
	"""
	
	suspended = "suspended"
	""" The authorization/request to act has been temporarily withdrawn but is expected to resume in the future.
	"""
	
	cancelled = "cancelled"
	""" The authorization/request to act has been terminated prior to the full completion of the intended actions.  No
	/// further activity should occur.
	"""
	
	completed = "completed"
	""" Activity against the request has been sufficiently completed to the satisfaction of the requester.
	"""
	
	enteredInError = "entered-in-error"
	""" This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
	"""
	
	unknown = "unknown"
	""" The authoring/source system does not know which of the status values currently applies for this observation.
	/// Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the
	/// authoring/source system does not know which.
	"""
}


class SynthesisType(object) {
	""" Types of combining results from a body of evidence (eg. summary data meta-analysis).

	URL: http://terminology.hl7.org/CodeSystem/synthesis-type
	ValueSet: http://hl7.org/fhir/ValueSet/synthesis-type
	"""
	
	stdMA = "std-MA"
	""" A meta-analysis of the summary data of estimates from individual studies or data sets.
	"""
	
	IPDMA = "IPD-MA"
	""" A meta-analysis of the individual participant data from individual studies or data sets.
	"""
	
	indirectNMA = "indirect-NMA"
	""" An indirect meta-analysis derived from 2 or more direct comparisons in a network meta-analysis.
	"""
	
	combinedNMA = "combined-NMA"
	""" An composite meta-analysis derived from direct comparisons and indirect comparisons in a network meta-analysis.
	"""
	
	range = "range"
	""" A range of results across a body of evidence.
	"""
	
	classification = "classification"
	""" An approach describing a body of evidence by categorically classifying individual studies (eg 3 studies showed
	/// beneft and 2 studied found no effect).
	"""
}


class TaskIntent(object) {
	""" Distinguishes whether the task is a proposal, plan or full order.

	URL: http://hl7.org/fhir/task-intent
	"""
	
	unknown = "unknown"
	""" The intent is not known.  When dealing with Task, it's not always known (or relevant) how the task was initiated
	/// - i.e. whether it was proposed, planned, ordered or just done spontaneously.
	"""
}


class TaskStatus(object) {
	""" The current status of the task.

	URL: http://hl7.org/fhir/task-status
	ValueSet: http://hl7.org/fhir/ValueSet/task-status
	"""
	
	draft = "draft"
	""" The task is not yet ready to be acted upon.
	"""
	
	requested = "requested"
	""" The task is ready to be acted upon and action is sought.
	"""
	
	received = "received"
	""" A potential performer has claimed ownership of the task and is evaluating whether to perform it.
	"""
	
	accepted = "accepted"
	""" The potential performer has agreed to execute the task but has not yet started work.
	"""
	
	rejected = "rejected"
	""" The potential performer who claimed ownership of the task has decided not to execute it prior to performing any
	/// action.
	"""
	
	ready = "ready"
	""" The task is ready to be performed, but no action has yet been taken.  Used in place of
	/// requested/received/accepted/rejected when request assignment and acceptance is a given.
	"""
	
	cancelled = "cancelled"
	""" The task was not completed.
	"""
	
	inProgress = "in-progress"
	""" The task has been started but is not yet complete.
	"""
	
	onHold = "on-hold"
	""" The task has been started but work has been paused.
	"""
	
	failed = "failed"
	""" The task was attempted but could not be completed due to some error.
	"""
	
	completed = "completed"
	""" The task has been completed.
	"""
	
	enteredInError = "entered-in-error"
	""" The task should never have existed and is retained only because of the possibility it may have used.
	"""
}


class TemplateStatusCodeLifeCycle(object) {
	""" Life cycle of the Status Code of a Template Design (Version)

	URL: urn:oid:2.16.840.1.113883.3.1937.98.5.8
	ValueSet: urn:oid:2.16.840.1.113883.3.1937.98.11.8
	"""
	
	draft = "draft"
	""" Design is under development (nascent).
	"""
	
	pending = "pending"
	""" Design is completed and is being reviewed.
	"""
	
	active = "active"
	""" Design has been deemed fit for the intended purpose and is published by the governance group.
	"""
	
	review = "review"
	""" Design is active, but is under review. The review may result in a change to the design. The change may
	/// necessitate a new version to be created. This in turn may result in the prior version of the template to be
	/// retired. Alternatively, the review may result in a change to the design that does not require a new version to
	/// be created, or it may result in no change to the design at all.
	"""
	
	cancelled = "cancelled"
	""" A drafted design is determined to be erroneous or not fit for intended purpose and is discontinued before ever
	/// being published in an active state.
	"""
	
	rejected = "rejected"
	""" A previously drafted design is determined to be erroneous or not fit for intended purpose and is discontinued
	/// before ever being published for consideration in a pending state.
	"""
	
	retired = "retired"
	""" A previously active design is discontinued from use. It should no longer be used for future designs, but for
	/// historical purposes may be used to process data previously recorded using this design. A newer design may or may
	/// not exist. The design is published in the retired state.
	"""
	
	terminated = "terminated"
	""" A design is determined to be erroneous or not fit for the intended purpose and should no longer be used, even
	/// for historical purposes. No new designs can be developed for this template. The associated template no longer
	/// needs to be published, but if published, is shown in the terminated state.
	"""
}


class TestReportActionResult(object) {
	""" The results of executing an action.

	URL: http://hl7.org/fhir/report-action-result-codes
	ValueSet: http://hl7.org/fhir/ValueSet/report-action-result-codes
	"""
	
	pass = "pass"
	""" The action was successful.
	"""
	
	skip = "skip"
	""" The action was skipped.
	"""
	
	fail = "fail"
	""" The action failed.
	"""
	
	warning = "warning"
	""" The action passed but with warnings.
	"""
	
	error = "error"
	""" The action encountered a fatal error and the engine was unable to process.
	"""
}


class TestReportParticipantType(object) {
	""" The type of participant.

	URL: http://hl7.org/fhir/report-participant-type
	ValueSet: http://hl7.org/fhir/ValueSet/report-participant-type
	"""
	
	testEngine = "test-engine"
	""" The test execution engine.
	"""
	
	client = "client"
	""" A FHIR Client.
	"""
	
	server = "server"
	""" A FHIR Server.
	"""
}


class TestReportResult(object) {
	""" The reported execution result.

	URL: http://hl7.org/fhir/report-result-codes
	ValueSet: http://hl7.org/fhir/ValueSet/report-result-codes
	"""
	
	pass = "pass"
	""" All test operations successfully passed all asserts.
	"""
	
	fail = "fail"
	""" One or more test operations failed one or more asserts.
	"""
	
	pending = "pending"
	""" One or more test operations is pending execution completion.
	"""
}


class TestReportStatus(object) {
	""" The current status of the test report.

	URL: http://hl7.org/fhir/report-status-codes
	ValueSet: http://hl7.org/fhir/ValueSet/report-status-codes
	"""
	
	completed = "completed"
	""" All test operations have completed.
	"""
	
	inProgress = "in-progress"
	""" A test operations is currently executing.
	"""
	
	waiting = "waiting"
	""" A test operation is waiting for an external client request.
	"""
	
	stopped = "stopped"
	""" The test script execution was manually stopped.
	"""
	
	enteredInError = "entered-in-error"
	""" This test report was entered or created in error.
	"""
}


class TestScriptRequestMethodCode(object) {
	""" The allowable request method or HTTP operation codes.

	URL: http://hl7.org/fhir/http-operations
	ValueSet: http://hl7.org/fhir/ValueSet/http-operations
	"""
	
	delete = "delete"
	""" HTTP DELETE operation.
	"""
	
	get = "get"
	""" HTTP GET operation.
	"""
	
	options = "options"
	""" HTTP OPTIONS operation.
	"""
	
	patch = "patch"
	""" HTTP PATCH operation.
	"""
	
	post = "post"
	""" HTTP POST operation.
	"""
	
	put = "put"
	""" HTTP PUT operation.
	"""
	
	head = "head"
	""" HTTP HEAD operation.
	"""
}


class TransactionMode(object) {
	""" A code that indicates how transactions are supported.

	URL: http://hl7.org/fhir/transaction-mode
	ValueSet: http://hl7.org/fhir/ValueSet/transaction-mode
	"""
	
	notSupported = "not-supported"
	""" Neither batch or transaction is supported.
	"""
	
	batch = "batch"
	""" Batches are  supported.
	"""
	
	transaction = "transaction"
	""" Transactions are supported.
	"""
	
	both = "both"
	""" Both batches and transactions are supported.
	"""
}


class TriggerType(object) {
	""" The type of trigger.

	URL: http://hl7.org/fhir/trigger-type
	ValueSet: http://hl7.org/fhir/ValueSet/trigger-type
	"""
	
	namedEvent = "named-event"
	""" The trigger occurs in response to a specific named event, and no other information about the trigger is
	/// specified. Named events are completely pre-coordinated, and the formal semantics of the trigger are not
	/// provided.
	"""
	
	periodic = "periodic"
	""" The trigger occurs at a specific time or periodically as described by a timing or schedule. A periodic event
	/// cannot have any data elements, but may have a name assigned as a shorthand for the event.
	"""
	
	dataChanged = "data-changed"
	""" The trigger occurs whenever data of a particular type is changed in any way, either added, modified, or removed.
	"""
	
	dataAdded = "data-added"
	""" The trigger occurs whenever data of a particular type is added.
	"""
	
	dataModified = "data-modified"
	""" The trigger occurs whenever data of a particular type is modified.
	"""
	
	dataRemoved = "data-removed"
	""" The trigger occurs whenever data of a particular type is removed.
	"""
	
	dataAccessed = "data-accessed"
	""" The trigger occurs whenever data of a particular type is accessed.
	"""
	
	dataAccessEnded = "data-access-ended"
	""" The trigger occurs whenever access to data of a particular type is completed.
	"""
}


class TypeDerivationRule(object) {
	""" How a type relates to its baseDefinition.

	URL: http://hl7.org/fhir/type-derivation-rule
	ValueSet: http://hl7.org/fhir/ValueSet/type-derivation-rule
	"""
	
	specialization = "specialization"
	""" This definition defines a new type that adds additional elements to the base type.
	"""
	
	constraint = "constraint"
	""" This definition adds additional rules to an existing concrete type.
	"""
}


class UDIEntryType(object) {
	""" Codes to identify how UDI data was entered.

	URL: http://hl7.org/fhir/udi-entry-type
	ValueSet: http://hl7.org/fhir/ValueSet/udi-entry-type
	"""
	
	barcode = "barcode"
	""" a barcodescanner captured the data from the device label.
	"""
	
	rfid = "rfid"
	""" An RFID chip reader captured the data from the device label.
	"""
	
	manual = "manual"
	""" The data was read from the label by a person and manually entered. (e.g.  via a keyboard).
	"""
	
	card = "card"
	""" The data originated from a patient's implant card and was read by an operator.
	"""
	
	selfReported = "self-reported"
	""" The data originated from a patient source and was not directly scanned or read from a label or card.
	"""
	
	unknown = "unknown"
	""" The method of data capture has not been determined.
	"""
}


class UnknownContentCode(object) {
	""" A code that indicates whether an application accepts unknown elements or extensions when reading resources.

	URL: http://hl7.org/fhir/unknown-content-code
	ValueSet: http://hl7.org/fhir/ValueSet/unknown-content-code
	"""
	
	no = "no"
	""" The application does not accept either unknown elements or extensions.
	"""
	
	extensions = "extensions"
	""" The application accepts unknown extensions, but not unknown elements.
	"""
	
	elements = "elements"
	""" The application accepts unknown elements, but not unknown extensions.
	"""
	
	both = "both"
	""" The application accepts unknown elements and extensions.
	"""
}


class UsageContextType(object) {
	""" A code that specifies a type of context being specified by a usage context.

	URL: http://terminology.hl7.org/CodeSystem/usage-context-type
	ValueSet: http://hl7.org/fhir/ValueSet/usage-context-type
	"""
	
	gender = "gender"
	""" The gender of the patient. For this context type, appropriate values can be found in the
	/// http://hl7.org/fhir/ValueSet/administrative-gender value set.
	"""
	
	age = "age"
	""" The age of the patient. For this context type, the value could be a range that specifies the applicable ages or
	/// a code from an appropriate value set such as the MeSH value set
	/// http://terminology.hl7.org/ValueSet/v3-AgeGroupObservationValue.
	"""
	
	focus = "focus"
	""" The clinical concept(s) addressed by the artifact. For example, disease, diagnostic test interpretation,
	/// medication ordering as in http://hl7.org/fhir/ValueSet/condition-code.
	"""
	
	user = "user"
	""" The clinical specialty of the context in which the patient is being treated - For example, PCP, Patient,
	/// Cardiologist, Behavioral Professional, Oral Health Professional, Prescriber, etc... taken from a specialty value
	/// set such as the NUCC Health Care provider taxonomy value set http://hl7.org/fhir/ValueSet/provider-taxonomy.
	"""
	
	workflow = "workflow"
	""" The settings in which the artifact is intended for use. For example, admission, pre-op, etc. For example, the
	/// ActEncounterCode value set http://terminology.hl7.org/ValueSet/v3-ActEncounterCode.
	"""
	
	task = "task"
	""" The context for the clinical task(s) represented by this artifact. For example, this could be any task context
	/// represented by the HL7 ActTaskCode value set http://terminology.hl7.org/ValueSet/v3-ActTaskCode. General
	/// categories include: order entry, patient documentation and patient information review.
	"""
	
	venue = "venue"
	""" The venue in which an artifact could be used. For example, Outpatient, Inpatient, Home, Nursing home. The code
	/// value may originate from the HL7 ServiceDeliveryLocationRoleType value set
	/// (http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType).
	"""
	
	species = "species"
	""" The species to which an artifact applies. For example, SNOMED - 387961004 | Kingdom Animalia (organism).
	"""
	
	program = "program"
	""" A program/project of work for which this artifact is applicable.
	"""
}


class Use(object) {
	""" Complete, proposed, exploratory, other.

	URL: http://hl7.org/fhir/claim-use
	ValueSet: http://hl7.org/fhir/ValueSet/claim-use
	"""
	
	claim = "claim"
	""" The treatment is complete and this represents a Claim for the services.
	"""
	
	preauthorization = "preauthorization"
	""" The treatment is proposed and this represents a Pre-authorization for the services.
	"""
	
	predetermination = "predetermination"
	""" The treatment is proposed and this represents a Pre-determination for the services.
	"""
}


class VisionBase(object) {
	""" A coded concept listing the base codes.

	URL: http://hl7.org/fhir/vision-base-codes
	ValueSet: http://hl7.org/fhir/ValueSet/vision-base-codes
	"""
	
	up = "up"
	""" top.
	"""
	
	down = "down"
	""" bottom.
	"""
	
	in = "in"
	""" inner edge.
	"""
	
	out = "out"
	""" outer edge.
	"""
}


class VisionEyes(object) {
	""" A coded concept listing the eye codes.

	URL: http://hl7.org/fhir/vision-eye-codes
	ValueSet: http://hl7.org/fhir/ValueSet/vision-eye-codes
	"""
	
	right = "right"
	""" Right Eye.
	"""
	
	left = "left"
	""" Left Eye.
	"""
}


class XPathUsageType(object) {
	""" How a search parameter relates to the set of elements returned by evaluating its xpath query.

	URL: http://hl7.org/fhir/search-xpath-usage
	ValueSet: http://hl7.org/fhir/ValueSet/search-xpath-usage
	"""
	
	normal = "normal"
	""" The search parameter is derived directly from the selected nodes based on the type definitions.
	"""
	
	phonetic = "phonetic"
	""" The search parameter is derived by a phonetic transform from the selected nodes.
	"""
	
	nearby = "nearby"
	""" The search parameter is based on a spatial transform of the selected nodes.
	"""
	
	distance = "distance"
	""" The search parameter is based on a spatial transform of the selected nodes, using physical distance from the
	/// middle.
	"""
	
	other = "other"
	""" The interpretation of the xpath statement is unknown (and can't be automated).
	"""
}
